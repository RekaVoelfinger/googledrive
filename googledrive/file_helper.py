from __future__ import print_function
import io
from googleapiclient.http import MediaIoBaseDownload

# TODO add file_name_list argument
def collect_files(service):
    # Call the Drive v3 API
    # files.list searches names and ids of the first "page_size" files from drive the user has access to.
    # search can be refined with query parameter # eg. "name = 'A01060.mp3'" and "sharedWithMe"

    # TODO rework query to use file_name_list argument
    query = "name = 'A01060.mp3' or name = 'A01044.mp3'"
    results = service.files().list(
        corpora="user",  # TODO To search in shared drive add parameter: driveId="1t7H5baSoNLZA_B5XZ-L6WYWDRw2sxdU9",
        includeItemsFromAllDrives="true",
        supportsAllDrives="true",
        q = query,
        pageSize=20, fields="nextPageToken, files(id, name)").execute()
    return results.get('files', [])


def download_all_files(service, file_list):
    if not file_list:
        print('No files found.')
    else:
        print('Download started')
        for item in file_list:
            file_id = item['id']
            file_name = item['name']
            print(u'Download {0} ({1})'.format(item['name'], item['id']))
            _download_file(service, file_id, file_name)


def _download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    # TODO download to separate directory
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    print("Download requested file: {0}".format(file_id))
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
