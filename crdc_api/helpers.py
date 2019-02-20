import pandas
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


def get_layout_file(filename):
    df = pandas.read_csv(INPUT_DIR+filename,
                         encoding='LATIN-1',
                         header=0,
                         names=['order', 'excel_column',
                                'column_name', 'description', 'module']
                         )

    df['table_name'] = df['module'].map(make_table_name)
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


def make_table_row_map(df, index, prefix):
    curr_table_name = ""
    table_row_map = {}

    for row in df.itertuples():

        if(tablenamify(row.table_name, prefix) != curr_table_name):
            curr_table_name = tablenamify(row.next_table_name, prefix)
            table_row_map[curr_table_name] = []

        if row.column_name != index:
            table_row_map[curr_table_name].append(row.column_name)

    return table_row_map
