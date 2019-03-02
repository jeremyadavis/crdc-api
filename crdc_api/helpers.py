import pandas
import subprocess
import time
from constants import (
    INPUT_DIR,
    OUTPUT_DIR,
    DB_SCHEMA
)

from utils import (
    make_table_name,
    create_directory,
    tablenamify,
    viewnameify,
    pretty_print,
)


from translator import (
    module_to_db_object,
    make_view_name
)


def get_layout_file(filename, config):
    df = pandas.read_csv(INPUT_DIR+filename,
                         encoding='LATIN-1',
                         header=0,
                         names=['order', 'excel_column',
                                'column_name', 'description', 'module']
                         )
    df['table_name'] = df['module'].apply(
        module_to_db_object, args=(config, "_table",))
    df['view_name'] = df['module'].apply(
        module_to_db_object, args=(config, ""))

    df['column_name'] = df['column_name'].map(lambda x: x.lower())
    df['view_column_name'] = df.apply(
        make_view_name, axis=1, args=(config,))

    df['is_first_column'] = df['table_name'] != df['table_name'].shift(1)
    df['is_last_column'] = df['table_name'] != df['table_name'].shift(-1)

    # print(df.head(200))

    return df


def get_data_file(filename, config, num_rows=None):
    if not(num_rows):
        print("WARNING! No Row Limiting for LEA_DATA")

    df = pandas.read_csv(INPUT_DIR+filename,
                         encoding='LATIN-1',
                         nrows=num_rows,
                         low_memory=False
                         )

    df.columns = df.columns.map(lambda x: x.lower())
    index_col = get_table_primary_key(config)
    df.set_index(index_col, inplace=True)

    return df


def get_table_primary_key(config):
    return config['tables']['primary_key']


def get_db_schema(config):
    return config['schema']


def make_table_row_map(df_layout, primary_key):
    curr_table_name = ""
    table_row_map = {}

    for row in df_layout.itertuples():
        if(row.is_first_column):
            curr_table_name = row.table_name
            table_row_map[curr_table_name] = []

        # Primary Key is used as index for df_data, so it will be auto included and set to first position
        if row.column_name != primary_key:
            table_row_map[curr_table_name].append(row.column_name)

    return table_row_map


def reset_containers():
    pretty_print("Removing Docker Containers and Volumes")
    subprocess.call(['docker-compose', 'down'])

    # out = subprocess.check_output(['echo', 'ehlo'])
    containers = subprocess.check_output(
        ['docker', 'ps', '-a', '-q'], universal_newlines=True)

    if(len(containers)):
        # print('removing containers', containers)
        subprocess.call(['docker', 'rm', '-f', containers])

    volumes = subprocess.check_output(
        ['docker', 'volume', 'ls', '-q'], universal_newlines=True).strip()

    if(len(volumes)):
        # print('removing volumes', volumes)
        subprocess.call(['docker', 'volume', 'rm', volumes])

    time.sleep(5)


def start_postgres_container():
    pretty_print("Started Postgres Docker Container")
    subprocess.call(['docker-compose', 'up', '-d', 'postgres'])

    time.sleep(5)


def start_graphql_engine_container():
    pretty_print("Started Graphql Engine Docker Container")
    subprocess.call(['docker-compose', 'up', '-d', 'graphql-engine'])


def module_to_view_name(module, prefix, translations):
    translated_module = translations['tables']['modules'].get(module, module)
    tableish = make_table_name(translated_module)

    return viewnameify(tableish, prefix, translations)
