#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:08:45 2019

@author: parashar
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import yaml
from getpass import getpass


def login(uname, passwd):

    # staackoverflow login
    driver.get(
        "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
    user_ip = driver.find_element_by_xpath(
        '//input[@id="email"]')
    user_ip.clear()
    user_ip.send_keys(uname)

    pass_ip = driver.find_element_by_xpath(
        '//input[@id="password"]')
    pass_ip.clear()
    pass_ip.send_keys(passwd)
    pass_ip.send_keys(Keys.ENTER)


def days_num():
    driver.implicitly_wait(10)
    # navigate to user profile
    driver.find_element_by_xpath(
        '//img[@class="-avatar js-avatar-me"]').click()
    # click on badge settings
    driver.find_element_by_xpath(
        '//a[@id="badge-card-settings"]').click()
    # search for fanatic badge
    driver.find_element_by_xpath(
        '//input[@placeholder="Search for a badge..."]').send_keys("fanatic")
    # get number text
    # num = driver.find_element_by_xpath(
    #     '//div[@class="grid grid__center fl1 s-badge--label"]').parent
    # num.find_element_by_xpath(
    #     '//div[@class="s-progress--bar"]')
    badge = driver.find_element_by_xpath(
        '//div[@data-badge-database-name="Fanatic"]')
    num = badge.get_attribute('innerText').splitlines()[0].replace('Fanatic - ','')
    print(num)
#    txt=badge.get_attribute('innerText')

# MAIN
if not os.path.exists('data.yaml'):
    user_id = input("Insert email_id:")
    passwd = getpass("Insert Password:")
    data = {'uname': user_id, 'password': passwd}
    with open('data.yaml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

data = yaml.load(open('data.yaml', "r", encoding='utf-8'))
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")

driver = webdriver.Chrome(chrome_options=options)

login(data['uname'], data['password'])
days_num()