'''
Download files from Google shared drive, where file names are given in a file called files_to_download.txt.
'''

from __future__ import print_function
from googleapiclient.discovery import build
from file_helper import collect_files
from file_helper import download_all_files
from login_helper import get_credentials

def main():
    service = build('drive', 'v3', credentials=get_credentials())
    # TODO get file names from files_to_download.txt
    file_list = collect_files(service)
    download_all_files(service, file_list)

if __name__ == '__main__':
    main()
