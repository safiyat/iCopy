#! /usr/bin/env python

from datetime import datetime
import hashlib
import md5
import os
import sys
import shutil


def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


def hash_bytestr_iter(bytesiter, hasher, ashexstr=True):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def walk(path):
    all_files = list()
    for root, subdirs, files in os.walk(path):
        if files:
            for f in files:
                all_files.append(os.path.join(root, f))
    return all_files

def get_det(afile):
    stats = os.stat(afile)
    size = sizeof_fmt(stats.st_size)
    atime = datetime.fromtimestamp(stats.st_atime).isoformat()
    ctime = datetime.fromtimestamp(stats.st_ctime).isoformat()
    mtime = datetime.fromtimestamp(stats.st_mtime).isoformat()
    name = afile
    digest = hash_bytestr_iter(file_as_blockiter(open(afile, 'rb')), hashlib.md5())
    return digest, {'name': name, 'size': size, 'atime': atime, 'ctime': ctime, 'mtime': mtime}


# Main part

path = '/Users/safiyat/Music'

l = dict()
c = dict()
for f in walk(path):
    h, d = get_det(f)
    if h not in l:
        l[h] = [d]
        continue
    l[h].append(d)
    c[h] = l[h]
