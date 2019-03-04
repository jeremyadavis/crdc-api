import yaml

from constants import (
    OUTPUT_DIR,
    MIGRATION_DIR,
)

from helpers import (
    get_layout_file,
    get_data_file,
    make_table_row_map,
    get_table_primary_key,
)

from utils import (
    execute_sql,
    pretty_print,
    get_num_files_in_dir
)

from translator import module_to_db_object


class DataMaker:
    def __init__(self, engine, data_files, config, db_config):
        self.engine = engine
        # self.data_file_index = config['data_file_index'].lower()
        # self.table_prefix = config['table_prefix']
        self.df_layout = get_layout_file(data_files['layout_file'], config)
        self.df_data = get_data_file(
            data_files['data_file'], config, db_config['row_insert_limit'])
        self.config = config
        self.primary_key = get_table_primary_key(config)
        self.db_schema = db_config['schema']

    def make_tables_and_files(self):
        table_map = make_table_row_map(
            self.df_layout,  self.primary_key)

        for table_name, df_columns in table_map.items():
            pretty_print(f"Making Table {table_name}", True)
            df_filtered = self.df_data.loc[:, df_columns]

            # CSV OUTPUT
            # df_filtered.to_csv(OUTPUT_DIR + "csv/" + table_name + ".csv")

            # DATABASE OUTPUT
            df_filtered.to_sql(table_name, self.engine,
                               #  if_exists="replace",
                               method="multi",
                               schema=self.db_schema,
                               chunksize=10000)

            execute_sql(
                self.engine, f"ALTER TABLE {self.db_schema}.\"{table_name}\" ADD PRIMARY KEY (\"{self.primary_key}\");")

    def make_views(self):
        view_statement = ""

        # print(self.df_layout.head(200))

        for row in self.df_layout.itertuples():
            if(row.is_first_column):
                view_statement = self.view_sql_start(row.view_name)

            if row.column_name != self.primary_key:
                view_statement += self.view_sql_column(
                    row.column_name, row.view_column_name, row.is_last_column)

            if(row.is_last_column):
                view_statement += self.view_sql_end(row.table_name)
                execute_sql(self.engine, view_statement)

    def view_sql_start(self, view_name):
        # view_name = viewnameify(
        #     view_name, self.table_prefix, self.translations)
        pretty_print(f"Making View {view_name}", True)
        return (
            f"CREATE OR REPLACE VIEW {self.db_schema}.\"{view_name}\"\n\tAS\n"
            "\tSELECT\n"
            "\t\t" + self.primary_key + " AS " + self.primary_key + ",\n"
        )

    def view_sql_column(self, table_column, view_column, is_last):
        sql_str = f"\t\t{table_column} AS {view_column}"
        sql_str += "\n" if is_last else ",\n"
        return sql_str

    def view_sql_end(self, table_name):
        return f"\tFROM\n\t\t{self.db_schema}.\"{table_name}\";\n\n"

    def make_migrations(self):

        self.make_migration_file(
            'create_all_views', self.make_view_migration_yaml)
        self.make_migration_file(
            'create_all_relationships', self.make_relationship_migration_yaml)
        self.make_migration_file(
            'access_roles', self.make_role_access_yaml)

    def make_migration_file(self, file_name, markup_method):
        migration_version = get_num_files_in_dir(MIGRATION_DIR) + 1
        migration_file_name = f"{migration_version}__{self.config['tables']['prefix']}{file_name}.up.yaml"
        pretty_print(f"Making Migration File {migration_file_name}", True)

        yaml_data = []

        for row in self.df_layout.itertuples():
            if(row.is_first_column):
                columns = [self.primary_key]

            if (row.view_column_name != self.primary_key):
                columns.append(row.view_column_name)

            if(row.is_last_column):
                view_migration_data = markup_method({
                    "view_name": row.view_name,
                    "schema": self.db_schema,
                    "module": row.module,
                    "columns": columns
                })

                # print('type', type(view_migration_data))
                if(view_migration_data):
                    if(isinstance(view_migration_data, (list,))):
                        for item in view_migration_data:
                            yaml_data.append(item)
                    else:
                        yaml_data.append(view_migration_data)

        with open(MIGRATION_DIR + migration_file_name, 'w') as yaml_file:
            noalias_dumper = yaml.dumper.SafeDumper
            noalias_dumper.ignore_aliases = lambda self, data: True
            yaml.dump(yaml_data, yaml_file, default_flow_style=False,
                      Dumper=noalias_dumper)
            yaml_file.close()

    def make_view_migration_yaml(self, args):
        return ({
            "args": {
                "name": args['view_name'],
                "schema": args['schema']
            },
            "type": "add_existing_table_or_view"
        })

    def make_relationship_migration_yaml(self, args):
        relationships_config = self.config['relationships']
        primary_module = relationships_config['primary_module']
        primary_to_secondary_map = relationships_config['primary_to_secondary_map']
        secondary_to_primary_field = relationships_config['secondary_to_primary_field']

        if((not relationships_config)):
            return None

        data = []
        relationships = []
        if(args['module'] == primary_module):
            for module, name in primary_to_secondary_map.items():
                relationships.append({
                    "name": name,
                    "remote_view_name": module_to_db_object(
                        module, self.config, "")
                })
        else:
            relationships.append({
                "name": secondary_to_primary_field,
                "remote_view_name": module_to_db_object(
                    primary_module, self.config, "")
            })

        for relationship in relationships:
            data.append({
                "args": {
                    "name": relationship['name'],
                    "table": {
                        "name": args['view_name'],
                        "schema": args['schema']
                    },
                    "using": {
                        "manual_configuration": {
                            "column_mapping": {
                                self.primary_key: self.primary_key
                            },
                            "remote_table": {
                                "name": relationship['remote_view_name'],
                                "schema": args['schema']
                            }
                        }
                    },
                },
                "type": "create_object_relationship"
            })

        return data

    def make_role_access_yaml(self, args):

        roles_config = self.config['roles']
        data = []

        # print('cols', args['columns'])
        for role, settings in roles_config.items():

            filter_config = settings["filter"]
            filter = {}

            if(filter_config):
                condition = {
                    filter_config["source_view_column"]: {
                        "_eq": filter_config["hasura_variable"]
                    }
                }
                # Curr Module is Source Module
                if(filter_config["source_module"] == args['module']):
                    filter = condition
                else:
                    # Curr Model isn't source module, so have to use relationship field to get to filter column
                    relationship_field = self.config['relationships']['secondary_to_primary_field']

                    filter = {
                        relationship_field: condition
                    }

            data.append({
                "args": {
                    "permission": {
                        "allow_aggregations": True,
                        "columns": args['columns'],
                        "filter": filter,
                        "limit": settings["limit"] if settings["limit"] else None
                    },
                    "role": role,
                    "table": {
                        "name": args['view_name'],
                        "schema": self.db_schema,
                    },
                },
                "type": "create_select_permission"
            })
        return data


# filter:
#     identification:
#         state:
#             _eq: X-Hasura-State

#             filter:
#     state:
#         _eq: X-Hasura-State
