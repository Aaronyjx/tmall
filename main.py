#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by aaron at 3/30/17

#System level
import locale

from lib.files import *
from lib.webs import *
from lib.excel import *
from lib.crawl import *
import setup


def inputKey():
    print('Please input keyword: ')
    keyword = input()
    if not keyword.isalnum:
        keyword.decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#    print('You have input: ', keyword)
    return keyword

def createFile():
    path = setup.DIR_PATH #'/home/aaron/py/test'
    filename = setup.FILE_NAME #'T' + time.strftime('%Y%m%d%H%M%S', time.localtime())

    file = Files(path, filename, '')

    file.createDir(str(path)) # Create Folder

    file.createFile(path, filename) # Create File
    return (path, filename)

def genLinks(keyword, path, filename):
    file = Files(path, filename, '')
    web = Webs()
    try:
        print('Searching page:  1 now')
        html = web.search(keyword)
        linklist = web.parse(html)
        linklist = '\n'.join(linklist)
        file.writeFile(path, filename, linklist)
        print('Search page:  1 is completed')

        print('Searching more now')
        for i in range(1, setup.PAGE):
            linklist = web.searchMore()
            linklist = '\n'.join(linklist)
            file.writeFile(path, filename, linklist)
            print('Search page: {0:2d} is completed'.format(i+1))

    except Exception:
        print('Failed')

    finally:
        setup.DRIVER.close()

def crawlAndWrite(path, filename):
    """Crawling and write to excel"""
    crawl = Crawl()
    read = Files(path, filename, '')
    excel = Excel()
    records = read.readFile(path, filename)
    for record in records:
        record = record.strip('\n')
        infos = crawl.crawler(record)
        for info in infos:
            url = info.get('url')
            comments = info.get('commentsInfo')
            for comment in comments:
                content = comment[0]
                user = comment[1]
                if len(comments) > 0:
                    excel.write_info((user, content, url), path, filename)

def cleanUp():
    """Clean up"""
    #Generate files list for clean up
    path = setup.DIR_PATH_FILE
    filename = setup.FILE_LIST # Create file in order to save file list
    file = Files(path, filename, '')
    file.createFile(path, filename)
    path = setup.DIR_PATH
    pathfile = setup.DIR_PATH_FILE
    file.fileList(path, pathfile, filename) # Generate file list

    file.fileRemove(path, pathfile, filename) # Remove file from folder

def main():
    """Main routine"""
    file = createFile() # Create folder and txt for save links

    keyword = inputKey() # input

    path = file[0]
    filename = file[1]
    genLinks(keyword, path, filename) # generate linklist

    crawlAndWrite(path, filename) # crawling link and write into excel one by one


#    cleanUp() # clean up after done

if __name__ == '__main__':
    main()