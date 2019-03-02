import json

from utils import (str2bool, clean_and_join_list)


GLOBAL_TRANSLATIONS = {
    "first": {
        "TOT": "TOTAL"
    },
    "second_to_last": {
        "HI": "HISPANIC",
        "AM": "AMERICAN_INDIAN",
        "AS": "ASIAN",
        "HP": "PACIFIC_ISLANDER",
        "BL": "BLACK",
        "WH": "WHITE",
        "TR": "MULTIRACIAL"
    },
    "last": {
        "M": "MALE",
        "F": "FEMALE",
        "IND": "INDICATOR",
        "WODIS": "WITHOUT_DISABILITY",
        "TOT": "TOTAL"
    }
}

POSTPROCESSING_CLEANUP = {
    "504": "prog504"
}


def translate_by_part_position(part, position, part_config):
    # print("translate_by_part_position", part, position)
    return part_config[position].get(
        part, GLOBAL_TRANSLATIONS[position].get(part, part))


def make_view_name(row, config):
    column_config = config['columns']
    part_config = column_config["part_positions"]
    modules_config = column_config['modules']
    general_config = column_config['general']
    column_split = row.column_name.upper().split("_")

    for index, part in enumerate(column_split):
        # print(f"Processing {part} at index {index}")

        # --- First Position
        if(index == 0):
            part = translate_by_part_position(part, "first", part_config)

        # --- Second to Last Position
        elif(len(column_split) - 2 == index):
            part = translate_by_part_position(
                part, "second_to_last", part_config)

        # --- Last Position
        elif(len(column_split) - 1 == index):
            part = translate_by_part_position(part, "last", part_config)

        # --- Config overrides by module
        module_switcher = modules_config.get(row.module, {})
        part = module_switcher.get(part, part)

        # --- General Config overrides
        column_split[index] = general_config.get(part, part)

    view_name = clean_and_join_list(column_split)

    # PostProcess to make invalid view_names valid
    for key, value in POSTPROCESSING_CLEANUP.items():
        if(view_name.startswith(key)):
            view_name = view_name.replace(key, value, 1)

    return view_name


def module_to_db_object(module, config, suffix):
    table_config = config['tables']

    t_mod = table_config['module_translations'].get(module, module.replace(
        ' ', '_').replace('-', '_').lower())

    table_name = ""
    if(isinstance(t_mod, dict)):
        table_name = table_config['prefix'] + \
            t_mod['value'] if str2bool(
                t_mod['should_prefix']) else t_mod['value']
    else:
        table_name = table_config['prefix'] + t_mod

    return table_name + suffix
