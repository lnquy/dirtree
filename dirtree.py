#!/usr/bin/python3
# Exercise project when learning Python =))
# DirTree recursively look for all child folders/files in a directory path and draw its directory tree to the console
# --------------------------
# @author: lnquy (Quy Le)
# @email: lnquy.it@gmail.com
# @date: Jul 11 2017
# --------------------------

import os
import sys
from os import listdir, path

BLUE = '\033[0;34m'
NC = '\033[0m'
SIZE = ("B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
folders_num = 0
files_num = 0


def pretty_size(fpath):
    s = path.getsize(fpath)
    i = 1
    while s // 1000 > 0:
        s /= 1000
        i += 1
    return ("%.1f" % s) + SIZE[i - 1]


def watcher(dpath, level):
    global folders_num, files_num
    try:
        for f in listdir(dpath):
            abs_path = path.join(dpath, f)
            if path.isdir(abs_path):
                folders_num += 1
                print(("  |" * level) + "  +--" + BLUE + f + NC)
                watcher(abs_path, level + 1)
            else:
                files_num += 1
                print(("  |" * level) + "  |--" + f + " - " + pretty_size(abs_path))
    except IOError:  # Permission denied
        pass


# Start
dir_path = os.environ["PWD"]
if len(sys.argv) >= 2:
    dir_path = sys.argv[1]
print(dir_path)
watcher(dir_path, 0)
print("\n" + str(folders_num) + (" folder" if folders_num <= 1 else " folders") + ", " +
      str(files_num) + (" file" if files_num <= 1 else " files"))
