import os

'''
Transform this
A01044.mp3
A01060.mp3
A04044.mp3
to this
"name = 'A01044.mp3' or name = 'A01060.mp3' or name = 'A04044.mp3'"
'''
def transform_input():
    file_names = 'files_to_download.txt'  # input()
    file_name_list = ""
    with open(file_names, 'r') as f:
        while True:
            lines = f.readlines()
            print(f"Lines read from {file_names} : {lines}")
            if not lines:
                break
            for line in lines:
                line = line.strip()
                line = "name = \'" + line + "\'" + " or "
                file_name_list += line
            print(f"Transformed list of files: {file_name_list}")
    file_name_list = file_name_list[:-4]
    return file_name_list


def preparation():
    if not os.path.exists('../downloads'):
        os.makedirs(os.path.join(os.path.abspath('..'), 'downloads'))
    location = os.path.join(os.path.abspath('..'), 'downloads')
    print(f"Download files from Google shared drive, where file names are given in a file called files_to_download.txt.\n"
          f"Copy files_to download.txt to \n{location}")
    ready = input("Are you ready? - Y or N\n")
    if ready == "Y":
        pass
#TODO finish preparation

