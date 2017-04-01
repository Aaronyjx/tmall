#!/usr/bin/env python
# -*- codning:utf-8 -*-
# Created by aaron at 3/30/17

#System level
import time
import os

class Files:
    """Define file handler"""
    def __init__(self, path, filename, content):
#        """Initial Folder name and File name"""
        self.path = path
        self.filename = filename
        self.content = content

    def createDir(self, path):
        """Create folder"""
        if not path.endswith('/'):
            path = path + '/'
        if not os.path.exists(path):
            os.makedirs(path)

    def createFile(self, path, filename):
        """Create File"""
        if not path.endswith('/'):
            filename = path + '/' + filename + '.txt'
        else:
            filename = path + filename + '.txt'

        with open(filename, 'wt') as f:
            f.write('')
            f.close()

    def writeFile(self, path, filename, content):
        """Write File"""
        if not path.endswith('/'):
            filename = path + '/' + filename + '.txt'
        else:
            filename = path + filename + '.txt'

        with open(filename, 'wt') as f:
            f.write(content)
            f.close()

    def fileList(self, path, pathfile, filename):
        """Generate filelist"""
        if path.endswith('/'):
            pos = path.rfind('/')
            path = path[:pos]
        else:
            path = path

        if not pathfile.endswith('/'):
            filename = pathfile + '/' + filename + '.txt'
        else:
            filename = pathfile + filename + '.txt'

        with open(filename, 'wt+') as f:
            for name in os.listdir(path):
                if os.path.isfile(os.path.join(path,name)):
                    f.write(name+'\n') # output file list except folder
            f.close()

    def fileRemove(self, path, pathfile, filename):
        if not path.endswith('/'):
            path = path + '/'

        if not pathfile.endswith('/'):
            filename = pathfile + '/' + filename + '.txt'
        else:
            filename = pathfile + filename + '.txt'

        with open(filename, 'r') as f:
            for name  in f:
                file = path + name
                os.remove(file.strip())
            f.close()