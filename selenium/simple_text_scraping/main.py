# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:05:59 2022

@author: scyth
"""

from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage') #mainly for linux
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome('C:/webdriver/chromedriver.exe',options=options)
    driver.get('http://automated.pythonanywhere.com')
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by='xpath',value='/html/body/div[1]/div/h1[1]')
    return element.text

print(main())
