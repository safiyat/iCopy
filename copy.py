#! /usr/bin/python

import os
import sys
import argparse
from iCopy.file import File
from iCopy.utilities import *


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


def main():

    parser = argparse.ArgumentParser(description='An intelligent tool to copy '
                                     '(and move, in future) files and '
                                     'directories from one location to '
                                     'another.')
    parser.add_argument('-s', '--source', type=str, required=True)
    parser.add_argument('-d', '--dest', type=str, required=True)

    args = parser.parse_args()

    src = args.source
    dest = args.dest

    file_list = list_contents(src)


    for f in file_list:
        fileobj = File(f)
        print "%s : %s" % (fileobj.get_filename().ljust(50),
                           fileobj.get_md5().ljust(60))

if __name__ == '__main__':
    sys.exit(main())
