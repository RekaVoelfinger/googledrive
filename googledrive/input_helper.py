'''
Transform this
A01044.mp3
A01060.mp3
A04044.mp3
to this
"name = 'A01044.mp3' or name = 'A01060.mp3' or name = 'A04044.mp3'"
'''
def transform_input(input_file_name):
    file_name_list = ""
    with open(input_file_name, 'r') as f:
        while True:
            lines = f.readlines()
            print(f"Lines read from {input_file_name} : {lines}")
            if not lines:
                break
            for line in lines:
                line = line.strip()
                line = "name = \'" + line + "\'" + " or "
                file_name_list += line
            print(f"Transformed list of files: {file_name_list}")
    file_name_list = file_name_list[:-4]
    # so it is not working: file_name_list = "'1t7H5baSoNLZA_B5XZ-L6WYWDRw2sxdU9' in parents and " + file_name_list[:-4]
    print(f"file_name_list with shared drive ID: {file_name_list} ")
    return file_name_list
