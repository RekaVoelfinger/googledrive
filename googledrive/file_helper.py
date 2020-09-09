from __future__ import print_function
import io
from googleapiclient.http import MediaIoBaseDownload


def collect_files(service, query):
    print("collect_files()")
    # Call the Drive v3 API
    # files.list searches names and ids of the first "page_size" files from drive the user has access to.
    # search can be refined with query parameter # eg. "name = 'A01060.mp3'" and "sharedWithMe"

    #query = "name = 'A01060.mp3' or name = 'A01044.mp3' or name = 'A04044.mp3'"
    #query = transform_input()
    print(f"collect_files() - query is '{query}'")
    results = service.files().list(
        corpora="user",  # TODO To search in shared drive add parameter: driveId="1t7H5baSoNLZA_B5XZ-L6WYWDRw2sxdU9",
        includeItemsFromAllDrives="true",
        supportsAllDrives="true",
        q = query,
        pageSize=20, fields="nextPageToken, files(id, name)").execute()
    collected_files = results.get('files', [])
    print(f"collect_files() - result is '{collected_files}'")
    return collected_files


def download_all_files(service, file_list):
    print("download_all_files()")
    if not file_list:
        print('download_all_files() - No files found.')
    else:
        print('download_all_files() - Download started')
        for item in file_list:
            file_id = item['id']
            file_name = item['name']
            print(f"download_all_files() - Download {item['name']} ({item['id']})")
            _download_file(service, file_id, file_name)


def _download_file(service, file_id, file_name):
    print(f"_download_file({file_name})")
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    print(f"_download_file({file_name}) - Download requested file with ID of {file_id}")
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"_download_file({file_name}) - Download {int(status.progress() * 100)}%.")
