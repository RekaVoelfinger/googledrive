from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload


# If modifying these scopes, delete the file token.pickle.
# Originaly was: SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def download_file(current_service, file_id):
    request = current_service.files().get_media(fileId=file_id)
    # original: fh = io.BytesIO()
    fh = io.FileIO("downloaded_file", 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    print("Download requested file_id: %s" % file_id)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

def load_creds():
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    service = build('drive', 'v3', credentials=load_creds())

    # Call the Drive v3 API
    # files.list searches and prints names and ids of the first 10 files from drive the user has access to.
    results = service.files().list(
        corpora="user", # TODO To search in shared drive add parameter: driveId="1t7H5baSoNLZA_B5XZ-L6WYWDRw2sxdU9",
        includeItemsFromAllDrives="true",
        supportsAllDrives="true",
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

    download_file(service, '1CEt3H89l4003eNmuznLI4oCsMYtbxg_j')


if __name__ == '__main__':
    main()
