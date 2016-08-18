#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-


# This script is used to dump the folder structure for content 
# analysis.  Source Folder and Destinations are hard coded. @see `root_path` and
# `target`


import os
import logging

logger = logging.getLogger('root')
FORMAT = "[%(levelname)s] %(asctime)s %(funcName)s:%(lineno)s - %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.INFO)


def ignore(path):
    return 'Working File' in path or \
    '.DS_Store' == path or 'Exercise File' in path 


# @param target - file handle for writing.
# @param path - path to recurse
def print_folder_contents(f, path, depth = 0):
    space = '' if depth == 0 else ' ' * (depth - 2)

    rel_path = os.path.relpath(path, root_path)
    
    if rel_path != '.':
        logger.debug(space + rel_path)
        f.write(space + rel_path + '\n')

    folders = [x  for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    for folder in folders:
        if not ignore(folder):
            print_folder_contents(f, os.path.join(path, folder), depth + 2)

# Actual
root_path = '/Volumes/Extension/Video Lessons'
filename = '/Users/royce/Desktop/VideoIndex.txt'

# Test
# root_path = '/Users/royce/Desktop/VIDEO COPY/'
# filename = '/Users/royce/Desktop/VideoIndexTest.txt'

f = open(filename, 'w')
f.truncate

print_folder_contents(f, root_path)
f.close

print('End.')

