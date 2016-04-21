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


class File(object):
    def __init__(self, path=None):
        if path is not None:
            self.set_filename(path)

    def set_filename(self, path):
        self.abspath = os.path.abspath(path)
        # self.relpath = self.abspath with head common with
        #                os.path.abspath('.') removed
        self.relpath = path
        self.md5sum = self.md5(self.abspath)
        self.size = os.path.getsize(self.abspath)
        self.atime = os.path.getatime(self.abspath)
        self.ctime = os.path.getctime(self.abspath)
        self.mtime = os.path.getmtime(self.abspath)

    def get_filename(self):
        return self.abspath

    def get_filesize(self):
        return self.size

    def get_fileatime(self):
        return self.atime

    def get_filectime(self):
        return self.ctime

    def get_filemtime(self):
        return self.mtime

    def get_filetime(self):
        return (self.get_fileatime(), self.get_filectime(),
                self.get_filemtime())

    def get_md5(self):
        return self.md5sum.hexdigest()

    def md5(self, path):
        md5object = hashlib.new('md5')
        BLOCKSIZE = 4096
        f = open(path)
        text = f.read(BLOCKSIZE)
        while text:
            md5object.update(text)
            text = f.read(BLOCKSIZE)
        return md5object


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


def main():
    path = sys.argv[1]

    file_list = list_contents(path)

    for f in file_list:
        fileobj = File(f)
        print "%s : %s" % (fileobj.get_filename().ljust(50),
                           fileobj.get_md5().ljust(60))


if __name__ == '__main__':
    sys.exit(main())
