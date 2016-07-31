# Remove redundant text on name.


import os
import shutil
import re
import sys


def ignore(path):
    return '.DS_Store' == path


def rename_in_folder(path):
    os.chdir(path)

    files = [x  for x in os.listdir('.') if not os.path.isdir(x)]
    lst = []
    index_name_map = {}
    for f in files:
        if not ignore(f):
            oldname = f
            m = re.search(r'-(\d+)', f)
            current_index = int(m.group(1))
            lst.append(current_index)
            index_name_map[current_index] = f
            # newname = str(int(m.group(1)) - actual_lowest).zfill(2) + ' - ' + \
            #     oldname.replace(m.group(0), '')
            # print(newname)
            # shutil.move(oldname, newname)

    new_index = 0
    for index in sorted(lst):
        newname = str(new_index).zfill(2) + ' - ' + index_name_map[index].replace('-{:d}'.format(index), '')
        print(newname)
        index += 1


    folders = [x  for x in os.listdir(path) if os.path.isdir(path + os.sep + x)]
    for folder in folders:
        rename_in_folder(path + os.sep + folder)


path = "/Users/royce/Downloads/Shell Script Tutorial - Bash Scripting for LinuxUnixBash"
rename_in_folder(path)