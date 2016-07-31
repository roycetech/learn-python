# Remove redundant text on name.


import os
import shutil


def ignore(path):
    return '.DS_Store' == path


def rename_in_folder(path, to_remove):
    os.chdir(path)

    files = [x  for x in os.listdir('.') if not os.path.isdir(x)]
    for f in files:
        if not ignore(f) and to_remove in f:
            oldname = f
            newname = f.replace(to_remove, '')
            print(newname)
            shutil.move(oldname, newname)

    folders = [x  for x in os.listdir(path) if os.path.isdir(path + os.sep + x)]
    for folder in folders:
        rename_in_folder(path + os.sep + folder, to_remove)


path = "/Users/royce/Downloads/Puppet vs. Chef Comparing Configuration Management Systems"
to_remove = ' - Puppet vs. Chef- Comparing Configuration Management Systems Envato Tuts+ Course'
# path = "/Users/royce/Downloads/@Video Courses/[Tuts Plus] Drawing Fantasy Creatures Digitally Video Tutorial-KTR"
# to_remove = 'Drawing Fantasy Creatures Digitally - '

rename_in_folder(path, to_remove)
