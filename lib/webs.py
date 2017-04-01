#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by aaron at 3/31/17

# System level
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
import sys

# Private
import config

class Webs:
    """Define web handler"""
    def __init__(self):
        self.shoplist = []
        self.linklist = []

    def search(self, keyword):
        """Search by keyword"""
        driver = config.DRIVER
        link = config.SEARCH_LINK
        driver.get(link)

        try: # Driver Chrome
            WebDriverWait(driver, config.TIMEOUT).until(
                EC.presence_of_element_located((By.ID, "mq"))
            )
        except TimeoutException:
            print('loading failed')

        try: # Input keyword
            element = driver.find_element_by_css_selector('#mq')
            for word in keyword:
                element.send_keys(word)
            element.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print('Can not find search box')

#        print('Searching now')

        try: # Search keyword
            WebDriverWait(driver, config.TIMEOUT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#J_ItemList div.productImg-wrap"))
            )
        except TimeoutException:
            print('Search failed')

        html = driver.page_source # return page source
        return html

    def parse(self, html):
        """Parse page source"""
        doc = pq(html) # PyQuery to process
        prods = doc('#J_ItemList .product').items() # Retrieve products
        for prod in prods:
            shop = prod.find('.productShop-name').text()
            href = prod.find('.productImg').attr('href')
            if shop and href:
                if not shop in self.shoplist:
                    href = 'https:' + href
                    self.shoplist.append(shop)
                    self.linklist.append(href)
        return self.linklist # Return Link list

    def searchMore(self):
        driver = config.DRIVER

#        try:
#            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#        except (WebDriverException, Exception) as e:
#            print(e)
#            print('Go to button of page failed')

#        driver.implicitly_wait(10)

        try:
            next = driver.find_element_by_css_selector('#content b.ui-page-num > a.ui-page-next')
#            actions = ActionChains(driver)
#            actions.move_to_element(next).perform()
            next.click()
        except NoSuchElementException:
            print('Search next page failed')

        try:
            WebDriverWait(driver, config.TIMEOUT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#J_ItemList div.productImg-wrap"))
            )
        except TimeoutException:
            print('Search failed')

        html = driver.page_source
        linklist = self.parse(html)
        return linklist