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
    viewnameify
)


def get_layout_file(filename, translations):
    df = pandas.read_csv(INPUT_DIR+filename,
                         encoding='LATIN-1',
                         header=0,
                         names=['order', 'excel_column',
                                'column_name', 'description', 'module']
                         )

    translated_modules = df['module'].map(
        lambda m: translations['tables']['modules'].get(m, m))

    # translated_modules.map(lambda m: print(
    #     'test', m, m in translations['tables']['noprefix']))
    # print('test', translated_modules)

    df['table_name'] = translated_modules.map(make_table_name)
    df['next_table_name'] = df['table_name'].shift(-1)

    df['column_name'] = df['column_name'].map(lambda x: x.lower())

    return df


def get_data_file(filename, index_col, num_rows=None):
    if not(num_rows):
        print("WARNING! No Row Limiting for LEA_DATA")

    df = pandas.read_csv(INPUT_DIR+filename,
                         encoding='LATIN-1',
                         nrows=num_rows,
                         low_memory=False
                         )

    df.columns = df.columns.map(lambda x: x.lower())
    df.set_index(index_col, inplace=True)

    return df


def make_table_row_map(df, index, prefix, translations):
    curr_table_name = ""
    table_row_map = {}

    for row in df.itertuples():
        # print('row.table_name', row.table_name)
        prefix_option = prefix if row.table_name not in translations[
            'tables']['noprefix'] else None
        if(tablenamify(row.table_name, prefix_option) != curr_table_name):
            prefix_option = prefix if row.next_table_name not in translations[
                'tables']['noprefix'] else None
            curr_table_name = tablenamify(row.next_table_name, prefix_option)
            table_row_map[curr_table_name] = []

        if row.column_name != index:
            table_row_map[curr_table_name].append(row.column_name)

    return table_row_map


def reset_containers():
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
    subprocess.call(['docker-compose', 'up', '-d', 'postgres'])

    time.sleep(5)


def start_graphql_engine_container():
    subprocess.call(['docker-compose', 'up', '-d', 'graphql-engine'])
