'''
Transform this
A01044.mp3
A01060.mp3
A04044.mp3
to this
"name = 'A01044.mp3' or name = 'A01060.mp3' or name = 'A04044.mp3'"
'''
def transform_input():
    file_names = 'file_name_list.txt' # input('Which files do you want to download?\nGive the name of the file where file names are listed: ')
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


