import json


def process_group(part, module):
    group_switcher = {
        "HI": "HISPANIC",
        "AM": "AMERICAN_INDIAN",
        "AS": "ASIAN",
        "HP": "PACIFIC_ISLANDER",
        "BL": "BLACK",
        "WH": "WHITE",
        "TR": "MULTIRACIAL"
    }

    return group_switcher.get(part, part)


def process_suffix(part, module):
    result = part

    if(part == 'M'):
        result = 'Male'
    elif(part == 'F'):
        result = 'Female'
    elif(part == 'IND'):
        result = 'Indicator'
    elif(part == 'WODIS'):
        result = 'WITHOUT_DISABILITY'
    elif(part == 'TOT'):
        result = 'TOTAL'
    return result


def make_meaningful_name(orig, module, translations):
    # print("\n", orig)
    # print('make_meaningful_name', module.replace(' ', ''))

    result_split = orig.upper().split("_")

    for index, part in enumerate(result_split):
        # print(f"Processing {part} at index {index}")

        processed_part = part
        # --- Prefix
        if(index == 0):
            processed_part = translations['columns']['prefix'].get(part, part)
            # processed_part = process_prefix(processed_part, module)

        # --- Second to Last
        elif(len(result_split) - 2 == index and processed_part in ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]):
            processed_part = process_group(processed_part, module)

        # --- Suffix
        elif(len(result_split) - 1 == index):
            processed_part = process_suffix(processed_part, module)

        # result_split[index] = process_by_module(processed_part, module)
        module_switcher = translations['columns']['module'].get(
            module.replace(' ', ''), {})
        processed_part = module_switcher.get(processed_part, processed_part)

        result_split[index] = translations['columns']['general'].get(
            processed_part, processed_part)

    cleaned_result = list(filter(lambda x: len(x) > 0, result_split))
    cleaned_result = list(map(lambda x: x.lower(), cleaned_result))
    meaningful_name = "_".join(cleaned_result)

    if(meaningful_name.startswith('504')):
        meaningful_name = meaningful_name.replace('504', 'prog504')

    # print(meaningful_name)
    return meaningful_name
