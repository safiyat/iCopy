#!/usr/bin/python
import os
import sys
import shutil


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


def log(final_list):
    fp = open('list_details.txt', 'w')
    for a in final_list:
        x = a[0][-40:].ljust(40)
        y = a[1][-40:].ljust(40)
        z = a[2]
        fp.write('...' + x + '    ' + '...' + y + '    ' + z + '\n')
    fp.close()


def copy_data(final_list):
    for s, d, status in final_list:
        if status == 'N':  # New
            shutil.copy2(s, d)

if len(sys.argv) != 3:
    print 'Usage: command source destination'
    exit()

src = sys.argv[1]
dest = sys.argv[2]
conf_count = 0
conf_list = []
final_list = []


if os.path.isdir(src):
    if src[-1] != os.sep:
        src += os.sep
    # if the src is a directory, dest too will be a directory.
    if dest[-1] != os.sep:
        dest += os.sep
    ######################################################################
    ls = os.listdir(src)
    rsourcefiles = []
    i = 0
    while True:
        try:
            a = ls[i]
            i += 1
            # print 'Processing: ' + a + ' ' + str(i)
        except Exception:
            break
        # if os.path.isdir(src + a.split(src)[-1]):
        #     print 'Expanding ' + src + a.split(src)[-1]
        #     templs = os.listdir(src + a.split(src)[-1])
        #     ls += [src + a.split(src)[-1] + os.sep + b for b in templs]
        # else:
        #     rsourcefiles.append(a)
        if os.path.isdir(src + a):
            # print 'Expanding ' + src + a
            templs = os.listdir(src + a)
            ls += [a + os.sep + b for b in templs]
        else:
            rsourcefiles.append(a)
    destfiles = []
    for a in rsourcefiles:
        destpath = dest + a
        if os.path.isfile(destpath):
            conf_count += 1
            # print str(conf_count) + ' 1Conflict between ' + a + ' and '\
            #     + destpath
            shash = os.popen('md5sum ' + src + a).read().split()[0]
            dhash = os.popen('md5sum ' + destpath).read().split()[0]
            if shash == dhash:
                status = 'D'  # Duplicate
            else:
                status = 'R'  # Revised
            conf_list.append([src + a, destpath, status])
            destfiles.append('')
        else:
            status = 'N'      # New
            destfiles.append(destpath)
        final_list.append([src + a, destpath, status])

else:   # source is file. Destination can be a directory or a file.
    if os.path.exists(dest):
        if os.path.isdir(dest):
            if dest[-1] != os.sep:
                dest += os.sep
            destfiles = [dest + src.split(os.sep)[-1]]
            status = 'N'
        else:
            conf_count += 1
            # print str(conf_count) + ' 2Conflict between ' + Color.RED\
            #     + src + Color.END + ' and ' + Color.YELLOW + dest + Color.END
            shash = os.popen('md5sum ' + src).read().split()[0]
            dhash = os.popen('md5sum ' + dest).read().split()[0]
            if shash == dhash:
                status = 'D'  # Duplicate
            else:
                status = 'R'  # Revised
            conf_list.append([src, dest])
        final_list.append([src, dest, status])

log(final_list)
copy_data(final_list)
"""
for a in final_list:
    if a[2] == 'N':
        print '##########'
    elif a[2] == 'R':
        print '$$$$$$$$$$'
    print a
"""
