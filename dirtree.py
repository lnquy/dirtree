# Exercise project when learning Python =))
# DirTree recursively look for all child folders/files in a directory path and draw its directory tree to the console
# --------------------------
# @author: lnquy (Quy Le)
# @email: lnquy.it@gmail.com
# @date: Jul 11 2017
# --------------------------

import os
from os import listdir, path

RED = '\033[0;31m'
BLUE = '\033[0;34m'
GREEN = '\033[0;32m'
CYAN = '\033[0;36m'
NC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
SIZE = ("B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")


def green(s):
    print(GREEN + s + NC)


def red(s):
    print(RED + s + NC)


def blue(s):
    print(BLUE + s + NC)


def pretty_size(fpath):
    s = path.getsize(fpath)
    i = 1
    while s // 1000 > 0:
        s /= 1000
        i += 1
    return ("%.1f" % s) + SIZE[i - 1]


def watcher(dpath, level):
    try:
        for f in listdir(dpath):
            abs_path = path.join(dpath, f)
            if path.isdir(abs_path):
                print(("  |" * level) + "  +--" + BLUE + f + NC)
                watcher(abs_path, level + 1)
            else:
                print(("  |" * level) + "  |--" + f + " - " + pretty_size(abs_path))
    except IOError:  # Permission denied
        pass

# Start
print("Welcome to DirTree!")
dir_path = input("Please enter the directory path: ")
if not dir_path:
    dir_path = os.getcwd()
print(dir_path)
watcher(dir_path, 0)
