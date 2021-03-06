from enum import Enum

DB_SCHEMA = "crdc"
DATABASE_URL = "postgresql://postgres:@localhost:5432/postgres"

CRDC_DATA_URL = "https://www2.ed.gov/about/offices/list/ocr/docs/2015-16-crdc-data.zip"
CRDC_DATA_FOLDER = "Data Files and Layouts/"


class CRDCFile(Enum):
    LeaLayout = "lea_layout.csv"
    LeaData = "lea_data.csv"
    SchoolLayout = "school_layout.csv"
    SchoolData = "school_data.csv"


CRDC_FILES = [
    {
        "needed_file_name": CRDCFile.LeaLayout.value,
        "extracted_path": CRDC_DATA_FOLDER+"CRDC 2015-16 LEA Data Record Layout.csv"},
    {
        "needed_file_name": CRDCFile.LeaData.value,
        "extracted_path": CRDC_DATA_FOLDER+"CRDC 2015-16 LEA Data.csv"},
    {
        "needed_file_name": CRDCFile.SchoolLayout.value,
        "extracted_path": CRDC_DATA_FOLDER+"CRDC 2015-16 School Data Record Layout.csv"},
    {
        "needed_file_name": CRDCFile.SchoolData.value,
        "extracted_path": CRDC_DATA_FOLDER+"CRDC 2015-16 School Data.csv"}
]

INPUT_DIR = "./data/"
OUTPUT_DIR = "./data/"
MIGRATION_DIR = f"{OUTPUT_DIR}migrations/"
