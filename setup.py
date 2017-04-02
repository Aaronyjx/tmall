#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by aaron at 3/30/17

# System level
import time
from selenium import webdriver

DIR_PATH = '/home/aaron/py/test' # Folder in order to save log file
DIR_PATH_FILE = '/home/aaron/py' # Folder in order to save file list
FILE_NAME = 'LOG-' + time.strftime('%Y%m%d%H%M%S', time.localtime()) # File name format
FILE_LIST = 'Filelist' # File name of file list
OUT_FILE = 'TmallInfo'

DRIVER = webdriver.Chrome()
TIMEOUT = 10
SEARCH_LINK = 'https://www.tmall.com/'
PAGE = 2
COUNT = 10


