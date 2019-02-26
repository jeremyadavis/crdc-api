import os
from utils import (
    create_directory,
    remove_directory,
    fetch_file,
    get_filename_from_url,
    unzip,
    rename_files,
    pretty_print
)
from constants import (
    CRDC_DATA_URL,
    CRDC_DATA_FOLDER,
    CRDC_FILES,
    INPUT_DIR,
    OUTPUT_DIR,
    MIGRATION_DIR
)


def needed_files_exists():
    if(os.path.isdir(INPUT_DIR)):
        curr_input_files = os.listdir(INPUT_DIR)
        needed_files_list = list(
            map(lambda x: x['needed_file_name'], CRDC_FILES))

        return set(needed_files_list).issubset(curr_input_files)
    else:
        return False


def extracted_files_exists(dir):
    extracted_files_list = list(
        map(lambda x: x['extracted_path'].replace(CRDC_DATA_FOLDER, ""), CRDC_FILES))
    curr_extracted_files = os.listdir(
        dir+CRDC_DATA_FOLDER) if os.path.isdir(dir+CRDC_DATA_FOLDER) else []

    return set(extracted_files_list).issubset(curr_extracted_files)


def setup_data():
    pretty_print("SETUP DATA")
    extract_directory = f"{INPUT_DIR}extracts/"

    """
    See if needed files currently exist in input directory.
    If not, see if extract file already exists correctly
    If not, retrieve and extract accordingly
    Move extracted files to correct directory and simplified filename
    Remove extra directory and files
    """
    if (needed_files_exists()):
        pretty_print("Needed Files Already Exist", True)
    else:
        if (extracted_files_exists(extract_directory)):
            pretty_print("Extract Already Exist", True)
        else:
            create_directory(extract_directory)
            pretty_print("Fetching CRDC Data From Public Website (34MB)", True)
            zip_file_name = get_filename_from_url(CRDC_DATA_URL)
            zip_file_name = fetch_file(
                CRDC_DATA_URL, extract_directory, zip_file_name)

            pretty_print("Extracting Zip At ", True,
                         extract_directory + zip_file_name)
            unzip(extract_directory+zip_file_name, extract_directory)

        pretty_print("Moving Files In Place", True)
        formatted_files_list = list(map(lambda x: {
                                    "src_path": x["extracted_path"], "dest_path": x["needed_file_name"]}, CRDC_FILES))
        rename_files(formatted_files_list, extract_directory, INPUT_DIR)

        pretty_print("Cleaning Up", True)
        remove_directory(extract_directory)

    # create_directory(OUTPUT_DIR, True)

    create_directory(MIGRATION_DIR, True)
    # pretty_print("Setup Data Complete", True)
