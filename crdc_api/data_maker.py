from constants import (
    OUTPUT_DIR,
    DB_SCHEMA
)

from helpers import (
    get_layout_file,
    get_data_file,
    make_table_row_map,
)

from utils import (
    tablenamify,
    viewnameify,
    execute_sql
)

from translator import make_meaningful_name

from sqlalchemy import text


class DataMaker:
    def __init__(self, engine, config, translations):
        self.engine = engine
        self.data_file_index = config['data_file_index'].lower()
        self.table_prefix = config['table_prefix']
        self.df_layout = get_layout_file(config['layout_file'], translations)
        self.df_data = get_data_file(
            config['data_file'], self.data_file_index, 1000)
        self.translations = translations

    def make_tables_and_files(self):
        table_map = make_table_row_map(
            self.df_layout,
            self.data_file_index,
            self.table_prefix,
            self.translations
        )

        for table_name, df_columns in table_map.items():
            print(f"    * Making Table {table_name}")
            df_filtered = self.df_data.loc[:, df_columns]

            # CSV OUTPUT
            # df_filtered.to_csv(OUTPUT_DIR + table_name + ".csv")

            # DATABASE OUTPUT
            # if table_name != 'sch_enrollment_table':
            df_filtered.to_sql(table_name, self.engine,
                               #  if_exists="replace",
                               method="multi",
                               schema=DB_SCHEMA,
                               chunksize=10000)

            execute_sql(
                self.engine, f"ALTER TABLE {DB_SCHEMA}.\"{table_name}\" ADD PRIMARY KEY (\"{self.data_file_index}\");")

    def make_views(self):
        curr_table_name = ""
        view_statement = ""

        for row in self.df_layout.itertuples():
            is_last_column = row.table_name != row.next_table_name

            # ====== Start View Create
            if(row.table_name != curr_table_name):
                curr_table_name = row.next_table_name

                view_statement = self.view_sql_start(curr_table_name)

            # ====== Create column names
            if row.column_name != self.data_file_index:
                # ====== Create View Field Names
                view_column = make_meaningful_name(
                    row.column_name, row.module, self.translations)
                # view_column = row.column_name
                view_statement += self.view_sql_column(
                    row.column_name, view_column, is_last_column)

            # ====== Finish table/view create
            if(is_last_column):
                view_statement += self.view_sql_end(curr_table_name)
                # print(view_statement)

                # if(curr_table_name != 'sch_enrollment_table'):
                execute_sql(self.engine, view_statement)

    def view_sql_start(self, view_name):
        prefix_option = self.table_prefix if not view_name in self.translations[
            'tables']['noprefix'] else None
        view_name = viewnameify(view_name, prefix_option)
        print(f"    * Making View {view_name}")
        return (
            f"CREATE OR REPLACE VIEW {DB_SCHEMA}.\"{view_name}\"\n\tAS\n"
            "\tSELECT\n"
            "\t\t" + self.data_file_index + " AS " + self.data_file_index + ",\n"
        )

    def view_sql_column(self, table_column, view_column, is_last):
        sql_str = f"\t\t{table_column} AS {view_column}"
        sql_str += "\n" if is_last else ",\n"
        return sql_str

    def view_sql_end(self, table_name):
        prefix_option = self.table_prefix if not table_name in self.translations[
            'tables']['noprefix'] else None
        return f"\tFROM\n\t\t{DB_SCHEMA}.\"{tablenamify(table_name, prefix_option)}\";\n\n"
