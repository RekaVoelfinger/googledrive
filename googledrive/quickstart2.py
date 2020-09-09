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


def main():
    if not os.path.exists('../downloads'): # TODO make it OS independent
        os.makedirs(os.path.join(os.path.abspath('..'), 'downloads'))

    location = os.path.join(os.path.abspath('..'), 'downloads')
    print(f"Download files from Google shared drive, where file names are given in a file called files_to_download.txt.\n"
          f"Copy files_to download.txt to \n{location}")

    if os.path.exists(os.path.join(location, "files_to_download.txt")):
        service = build('drive', 'v3', credentials=get_credentials())
        os.chdir(location)
        file_list = collect_files(service, transform_input())
        print(f"Files to be download: {file_list}")
        download_all_files(service, file_list)
        print(f"All files are downloaded to {location}")

    else:
        print(f"files_to download.txt is not there {location}") # TODO it needs waiting time or interaction
        exit()

if __name__ == '__main__':
    main()

