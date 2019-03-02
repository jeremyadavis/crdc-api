import json
from datetime import datetime

from constants import (
    OutputOption,
    CRDCFile
)
from helpers import reset_containers, start_postgres_container, start_graphql_engine_container
from setup_data import setup_data
from setup_db import setup_db
from data_maker import DataMaker
from utils import pretty_print


def main():
    start = datetime.utcnow()

    print("\n\n\n============ BETTER CRDC ============")
    # reset_containers()
    # start_postgres_container()

    setup_data()
    engine = setup_db()

    pretty_print("CREATE LEA ARTIFACTS")
    lea_files = {
        'layout_file': CRDCFile.LeaLayout.value,
        'data_file': CRDCFile.LeaData.value,
    }
    lea_config = json.load(open('./crdc_api/lea_config.json'))
    lea_maker = DataMaker(engine, lea_files, lea_config)
    lea_maker.make_tables_and_files()
    lea_maker.make_views()
    # lea_maker.make_migrations()

    # pretty_print("CREATE SCHOOL ARTIFACTS")
    # school_config = {
    #     'layout_file': CRDCFile.SchoolLayout.value,
    #     'data_file': CRDCFile.SchoolData.value,
    #     'data_file_index': 'COMBOKEY',
    #     'table_prefix': 'sch_'
    # }
    # school_translations = open(
    #     './crdc_api/school_translations.json')
    # school_maker = DataMaker(engine, school_config,
    #                          json.load(school_translations))
    # school_maker.make_tables_and_files()
    # school_maker.make_views()
    # school_maker.make_migrations()

    # start_graphql_engine_container()

    print("\n\n=====================================\n")
    print(f"Program Completed in {datetime.utcnow() - start}\n\n\n")


if __name__ == '__main__':
    main()
