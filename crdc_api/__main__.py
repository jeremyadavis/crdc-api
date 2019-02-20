import json
from datetime import datetime

from constants import (
    OutputOption,
    CRDCFile
)
from setup_data import setup_data
from setup_db import setup_db
from data_maker import DataMaker


def main():
    start = datetime.utcnow()

    print("\n\n\n============ BETTER CRDC ============")
    setup_data()
    engine = setup_db()

    # print("--- STEP 3: CREATE LEA ARTIFACTS")
    lea_config = {
        'layout_file': CRDCFile.LeaLayout.value,
        'data_file': CRDCFile.LeaData.value,
        'data_file_index': 'LEAID',
        'table_prefix': 'lea_'
    }

    lea_column_translations = open('./crdc_api/lea_column_translations.json')
    lea_maker = DataMaker(engine, lea_config,
                          json.load(lea_column_translations))
    lea_maker.make_tables_and_files()
    lea_maker.make_views()

    print("--- STEP 4: CREATE SCHOOL ARTIFACTS")
    school_config = {
        'layout_file': CRDCFile.SchoolLayout.value,
        'data_file': CRDCFile.SchoolData.value,
        'data_file_index': 'COMBOKEY',
        'table_prefix': 'sch_'
    }
    school_column_translations = open(
        './crdc_api/school_column_translations.json')
    school_maker = DataMaker(engine, school_config,
                             json.load(school_column_translations))
    school_maker.make_tables_and_files()
    school_maker.make_views()

    print(f"Program Completed in {datetime.utcnow() - start}\n")
    print("=====================================\n\n\n")


if __name__ == '__main__':
    main()
