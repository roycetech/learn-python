#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-


# This script is used to dump the folder structure for content 
# analysis.  File is dumped on the desktop.


import glob
import os


def ignore(path):
    return 'Working File' in path or \
    '.DS_Store' == path or 'Exercise File' in path 


# @param target - file handle for writing.
# @param path - path to recurse
def printFolderContents(target, path, depth = 0):
    if depth == 0:
        space = ''
    else:
        space = '  ' * depth

    # print('D' + space + path)
    short_folder_name = path + os.linesep
    global root_path

    # print(root_path)

    short_folder_name = short_folder_name.replace(root_path, '')
    print(short_folder_name)
    target.write('D' + space + short_folder_name)

    files = [x  for x in os.listdir(path) if not os.path.isdir(path + os.sep + x)]
    for f in files:
        if not ignore(f):
            pass
            # print('F' + space + '  ' + f)

    folders = [x  for x in os.listdir(path) if os.path.isdir(path + os.sep + x)]
    for folder in folders:
        if not ignore(folder):
            printFolderContents(target, path + os.sep + folder, depth + 2)


root_path = '/Volumes/Extension/Video Lessons'
target = open('/Users/royce/Desktop/VideoIndex.txt', 'w')
target.truncate
# printFolderContents('/Users/royce/Desktop/VIDEO COPY')
printFolderContents(target, root_path)
target.close

# path = '/Volumes/Extension/Video Lessons/'
# path = '/Users/royce/Desktop/VIDEO COPY/'


print('End.')

