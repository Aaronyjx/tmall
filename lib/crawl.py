#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by aaron at 4/1/17

# System level
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import sys

# Private
import config

class Crawl:
    """Crawling web"""
#    def __init__(self):

    def crawler(self, url):
        """Main crawler"""
        infos = self.crawlInfo(url)
        for info in infos:
            url = info.get('url')
            commentsInfo = info.get('commentsInfo')
            for commentInfo in commentsInfo:
                commentContent = commentInfo[0]
                commentUser = commentInfo[1]
                print('commentUser', commentUser)
#                if len(commentsInfo) > 0 and not repeatExcel(commentUser):
#                    writeFile()


    def crawlInfo(self,url):
        """Crawling information"""
        info = []

        if not url.startswith('http'):
            url = 'https:' + url

        html = self.crawlPage(url)
        if html:
            doc = pq(html)
            items = doc('#J_TjWaterfall > li')
            for item in items.items():
                print(item)
                url = item.find('a').attr('href')
                if not url.startswith('http'):
                    url = 'https:' + url
                commentsInfo = []
                comments = item.find('p').items()
                for comment in comments:
                    commentUser = comment.find('b').remove().text()
                    commentContent = comment.text()
                    anonymousStr = config.ANONYMOUS_STR
                    commentsInfo.append((commentContent,commentUser))
                info.append({'url': url, 'commentsInfo': commentsInfo})
            return info
        else:
            return []

    def crawlPage(self, url):
        driver = config.DRIVER
        try:
            driver.get(url)
            WebDriverWait(driver, config.TIMEOUT).until(
                EC.presence_of_element_located((By.ID, "J_TabBarBox"))
            )
        except TimeoutException:
            print('Search page failed')

        if self.pageDown(driver):
            return driver.page_source
        else:
            print('Crawl information failed')

    def pageDown(self, driver):
        """Page Down"""
        count = 1
        result = self.pageBottom(driver, count)
        while not result:
            count = count + 1
            if count == config.COUNT:
                return False
            result = self.pageBottom(driver, count)
        return True

    def pageBottom(self, driver, i):
        """Go to bottom"""
        try:
            js = "window.scrollTo(0," + str(i * i * 300) + ")"
            driver.execute_script(js)
        except WebDriverException:
            print('Page down failed')
            return False

        driver.implicitly_wait(5)

        try:
            driver.find_element_by_css_selector('#J_TjWaterfall li')
        except NoSuchElementException:
            print('Locate information failed')
            return False
        return True


