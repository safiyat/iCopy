import os
import time
import hashlib


class File(object):
    """A class to maintain and manage the metadata of a file/directory."""
    def __init__(self, path=None):
        """
        Initialize a file object.

        path: [str] Path to the file being initialized.
        """
        if path is not None:
            self.set_filename(path)
        else:
            self.abspath = None
            self.relpath = None
            self.md5sum = None
            self.size = None
            self.atime = None
            self.ctime = None
            self.mtime = None

    def set_filename(self, path):
        self.abspath = os.path.abspath(path)
        # relpath needs fixing. It can be computed from one more argument.
        # Lets call that parameter the root directory.
        self.relpath = os.path.commonprefix([self.abspath,
                                             os.path.abspath('.')])
        self.md5sum = self.md5(self.abspath)
        self.size = os.path.getsize(self.abspath)
        self.atime = os.path.getatime(self.abspath)
        self.ctime = os.path.getctime(self.abspath)
        self.mtime = os.path.getmtime(self.abspath)

    def get_filename(self):
        return self.abspath

    def get_relpath(self):
        return self.relpath

    def get_filesize(self):
        return self.size

    def get_fileatime(self):
        return time.ctime(self.atime)

    def get_filectime(self):
        return time.ctime(self.ctime)

    def get_filemtime(self):
        return time.ctime(self.mtime)

    def get_filetime(self):
        return (self.get_fileatime(), self.get_filectime(),
                self.get_filemtime())

    def get_md5(self):
        return self.md5sum.hexdigest()

    def md5(self, path):
        md5object = hashlib.new('md5')
        BLOCKSIZE = 4096

        if os.path.isdir(path):
            return md5object

        f = open(path)
        text = f.read(BLOCKSIZE)
        while text:
            md5object.update(text)
            text = f.read(BLOCKSIZE)
        return md5object
