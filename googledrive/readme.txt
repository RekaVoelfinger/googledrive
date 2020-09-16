 
googledrive project
-------------------
16/09/2020

DESCRIPTION:
Downloads files from Google shared drive, where file names are given in a file called files_to_download.txt.
Based on the google drive api https://developers.google.com/drive/api/v3/quickstart/python 

Structur:

googledrive
googledrive/credentials.json
googledrive/download_from_googledrive.py
googledrive/file_helper.py
googledrive/input_helper.py
googledrive/login_helper.py
googledrive/quickstart_orig.py
googledrive/readme.txt
googledrive/requirements.txt
googledrive/token.pickle


HOW TO USE:

Create virtual environment:
>python -m venv /path/to/venv

Activate virtual environment:
>/path/to/venv/Scripts/activate.bat

Install depedencies:
>pip install -r path/to/project/requirements.txt

Run script:
>py googledrive/download_from_googledrive.py