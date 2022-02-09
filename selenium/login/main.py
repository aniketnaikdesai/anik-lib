# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:06:29 2022

@author: scyth
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage') #mainly for linux
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome('C:/webdriver/chromedriver.exe',options=options)
    driver.get('http://automated.pythonanywhere.com/login/')
    return driver

def clean_text(text):
    '''Extract only the temperature from the text'''
    return float(text.split(': ')[1])

def main():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(by='id',value='id_username').send_keys('automated')
    time.sleep(1)
    driver.find_element(by='id',value='id_password')\
        .send_keys('automatedautomated'+  Keys.RETURN)
    
    driver.find_element(by='xpath',value='/html/body/nav/div/a').click()
    time.sleep(1)
    
    print(driver.current_url)
    
    


print(main())