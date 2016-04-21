#! /usr/bin/python

import os
import sys
import hashlib


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def list_contents(path='.', full_list=None):
    path = os.path.abspath(path)
    contents = os.listdir(path)
    if full_list is None:
        full_list = []
    for entry in contents:
        cur_path = os.path.join(path, entry)
        if os.path.isfile(cur_path):
            full_list.append(cur_path)
        elif os.path.isdir(cur_path):
            list_contents(cur_path, full_list)
        else:
            print "%s failed." % (cur_path)
    full_list.sort()
    return full_list


def md5(path):
    md5object = hashlib.new('md5')
    BLOCKSIZE = 4096
    path = os.path.abspath(path)
    f = open(path)
    text = f.read(BLOCKSIZE)
    while text:
        md5object.update(text)
        text = f.read(BLOCKSIZE)
    return md5object.hexdigest()


def main():
    path = sys.argv[1]

    file_list = list_contents(path)

    for f in file_list:
        md5sum = md5(f)
        print "%s : %s" % (f.ljust(50), md5sum.ljust(60))


if __name__ == '__main__':
    sys.exit(main())
