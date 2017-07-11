# Exercise project when learning Python =))
# DirTree recursively look for all child folders/files in a directory and draw its directory tree to the console
# --------------------------
# @author: lnquy
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


def green(s):
    print(GREEN + s + NC)


def red(s):
    print(RED + s + NC)


def blue(s):
    print(BLUE + s + NC)


def watcher(dpath, level):
    try:
        level += 1
        for f in listdir(dpath):
            abs_path = path.join(dpath, f)
            if path.isdir(abs_path):
                blue(("  |" * (level - 1)) + "  +--" + f)
                watcher(abs_path, level)
            else:
                print(("  |" * (level - 1)) + "  |--" + f + " - " + str(path.getsize(abs_path)))
    except IOError:  # Permission denied
        pass

# Start
print("Welcome to DirTree!")
dir_path = input("Please enter the directory path: ")
if not dir_path:
    dir_path = os.getcwd()
print("Dir: ", dir_path)
watcher(dir_path, 0)

