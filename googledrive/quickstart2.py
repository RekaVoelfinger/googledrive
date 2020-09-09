'''
Download files from Google shared drive, where file names are given in a file called files_to_download.txt.
'''

from __future__ import print_function
from googleapiclient.discovery import build
from file_helper import collect_files
from file_helper import download_all_files
from login_helper import get_credentials
from input_helper import transform_input
import os


root_directory = os.path.abspath('..')
input_file_name = "files_to_download.txt"


def print_usage():
    print(
        f"Download files from Google shared drive, where file names are given in a file called {input_file_name}.\n"
        f"Please, create {input_file_name} in {root_directory}")


def check_target_dir():
    target_location = 'downloads'
    if not os.path.exists(target_location):
        os.makedirs(target_location)
    return target_location


def main():
    print(f"Download files from Google shared drive")
    service = build('drive', 'v3', credentials=get_credentials())

    os.chdir(root_directory)
    target_dir = check_target_dir()

    if os.path.exists(input_file_name):
        file_list = collect_files(service, transform_input(input_file_name))
        print(f"Files to be download: {file_list}")
        download_all_files(service, file_list)
        print(f"All files are downloaded to {target_dir}")

    else:
        print(f"{input_file_name} does not exist")
        print_usage()
        exit()

if __name__ == '__main__':
    main()

