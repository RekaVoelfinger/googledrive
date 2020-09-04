'''
Transform this
A01044.mp3
A01060.mp3
A04044.mp3
to this
"name = 'A01044.mp3' or name = 'A01060.mp3' or name = 'A04044.mp3'"
'''
def transform_input():
    file_name_list = 'file_name_list.txt' # input('Which files do you want to download?\nGive the name of the file where file names are listed: ')
    f = open(file_name_list, 'r')
    lines = f.read().split("\n")
    f.close()

    for l in range(len(lines)-1):
        lines[l] = "name = " + lines[l] + " or "
        l+=1
    #lines.insert(len(lines), '\"name = ')
    print(lines)


transform_input()
