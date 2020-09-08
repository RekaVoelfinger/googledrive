'''
Download files from Google shared drive, where file names are given in a file called files_to_download.txt.
'''

from __future__ import print_function
from googleapiclient.discovery import build
from file_helper import collect_files
from file_helper import download_all_files
from login_helper import get_credentials
from input_helper import transform_input


def main():
    print("Download files from Google shared drive, where file names are given in a file called files_to_download.txt.")
    service = build('drive', 'v3', credentials=get_credentials())
    file_list = collect_files(service, transform_input())
    print(f"Files to be download: {file_list}")
    download_all_files(service, file_list)
    print("All files are downloaded")

if __name__ == '__main__':
    main()
