#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by aaron at 3/30/17

#System level
import sys
import locale

#Private
import config
from lib.files import *
from lib.webs import *


def inputKey():
    print('Please input keyword: ')
    keyword = input()
    if not keyword.isalnum:
        keyword.decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#    print('You have input: ', keyword)
    return keyword


def main():
    """Main routine"""
    path = config.DIR_PATH #'/home/aaron/py/test'
    filename = config.FILE_NAME #'T' + time.strftime('%Y%m%d%H%M%S', time.localtime())

    file = Files(path, filename, '')

    file.createDir(str(path)) # Create Folder

    file.createFile(path, filename) # Create File

    keyword = inputKey()
    web = Webs()
    try:
        print('Searching page:  1 now')
        html = web.search(keyword)
        linklist = web.parse(html)
        linklist = '\n'.join(linklist)
        file.writeFile(path, filename, linklist)
        print('Search page:  1 is completed')

        print('Searching more now')
        for i in range(1, config.PAGE):
            linklist = web.searchMore()
            linklist = '\n'.join(linklist)
            file.writeFile(path, filename, linklist)
            print('Search page: {0:2d} is completed'.format(i+1))

    except Exception:
        print('Failed')

    finally:
        config.DRIVER.close()


# Generate files list for clean up
#    path = config.DIR_PATH_FILE
#    filename = config.FILE_LIST # Create file in order to save file list
#    file.createFile(path, filename)
#    path = config.DIR_PATH
#    pathfile = config.DIR_PATH_FILE
#    file.fileList(path, pathfile, filename) # Generate file list

# clean up
#    file.fileRemove(path, pathfile, filename) # Remove file from folder

if __name__ == '__main__':
    main()