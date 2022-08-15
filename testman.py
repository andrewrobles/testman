from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import configparser

import json

class Testman:
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

    def submit(self, problem, filename):
        file = open(filename, 'r')
        solution = file.read()
        file.close()
        self._browser.get('https://leetcode.com/problems/{}/'.format(problem))

        sleep(2)
        select = self._browser.find_element_by_css_selector("div[role='combobox']")
        select.click()
        sleep(1)
        python = self._find_element_by_text('Python3')
        python.click()

        sleep(2)
        codeMirror = self._browser.find_element_by_css_selector('.CodeMirror textarea')

        action_chains = ActionChains(self._browser)
        action_chains.click(codeMirror).perform()
        action_chains.send_keys(solution).perform()

    def _find_element_by_text(self, text):
        return self._browser.find_element_by_xpath("//*[text()='{}']".format(text)) 

    def _find_elements_by_text(self, text):
        return self._browser.find_elements_by_xpath("//*[text()='{}']".format(text))
