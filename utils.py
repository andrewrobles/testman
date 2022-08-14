from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import configparser

import json

class Bot:
    def __init__(self):
        file = open('settings.json', 'r')
        settings = json.load(file)
        file.close()

        username = settings['username']
        password = settings['password']

        browser = webdriver.Firefox()
        self._browser = browser
        self._browser.implicitly_wait(10)
        self._base_url = 'https://www.leetcode.com/accounts/login/'
        self._browser.get(self._base_url)
        sleep(1)
        self.login(username, password)

    def login(self, username, password):
        username_input = self._browser.find_element_by_css_selector("input[name='login']")
        password_input = self._browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(1)
        login_button = self._browser.find_element_by_xpath("//button[@id='signin_btn']")
        login_button.click()
        sleep(5)  

    def load_amazon_questions(self):
        self._browser.get('https://leetcode.com/company/amazon')

    def _find_element_by_text(self, text):
        return self._browser.find_element_by_xpath("//*[text()='{}']".format(text)) 

    def _find_elements_by_text(self, text):
        return self._browser.find_elements_by_xpath("//*[text()='{}']".format(text))
