#!/usr/bin/python3
# Exercise project when learning Python =))
# DirTree recursively look for all child folders/files in a directory path and draw its directory tree to the console
# --------------------------
# @author: lnquy (Quy Le)
# @email: lnquy.it@gmail.com
# @date: Jul 11 2017
# --------------------------

import os
import sys, getopt
from os import listdir, path

BLUE = '\033[0;34m'
NC = '\033[0m'
SIZE = ("B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
folders_num = 0
files_num = 0
MAX_DEEP_DIRS = 9000  # It's over 9000 :)


def pretty_size(fpath):
    s = path.getsize(fpath)
    i = 1
    while s // 1000 > 0:
        s /= 1000
        i += 1
    return ("%.1f" % s) + SIZE[i - 1]


def watcher(dpath, level, watch_level):
    global folders_num, files_num
    try:
        for f in listdir(dpath):
            abs_path = path.join(dpath, f)
            if path.isdir(abs_path):
                folders_num += 1
                print(("  |" * level) + "  +--" + BLUE + f + NC)
                if level < watch_level - 1:
                    watcher(abs_path, level + 1, watch_level)
                else:
                    print(("  |" * (level + 1)) + "  +--...")
            else:
                files_num += 1
                print(("  |" * level) + "  |--" + f + " - " + pretty_size(abs_path))
    except IOError:  # Permission denied
        pass


def parse_watch_level(argv):
    try:
        opts, args = getopt.getopt(argv, "l:")
    except getopt.GetoptError:
        print("Failed to parse watcher level. Use default value: " + str(MAX_DEEP_DIRS))
        return MAX_DEEP_DIRS
    for opt, arg in opts:
        if opt == "-l":
            return int(arg)
    return MAX_DEEP_DIRS


def main(argv):
    watch_level = parse_watch_level(argv)
    print("Max watcher level: " + str(watch_level))

    dir_path = os.environ["PWD"]
    # TODO
    #if len(sys.argv) >= 2:
    #    dir_path = sys.argv[1]
    print(dir_path)
    watcher(dir_path, 0, watch_level)
    print("\n" + str(folders_num) + (" folder" if folders_num <= 1 else " folders") + ", " +
          str(files_num) + (" file" if files_num <= 1 else " files"))


if __name__ == "__main__":
    main(sys.argv[1:])
