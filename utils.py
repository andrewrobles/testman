from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

class InstagramBot:
    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(10)
        self._base_url = 'https://www.leetcode.com/accounts/login/'
        self._browser.get(self._base_url)
        sleep(1)

    def login(self, username, password):
        username_input = self._browser.find_element_by_css_selector("input[name='login']")
        password_input = self._browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(1)
        login_button = self._browser.find_element_by_xpath("//button[@id='signin_btn']")
        login_button.click()
        sleep(5)  

    def _find_element_by_text(self, text):
        return self._browser.find_element_by_xpath("//*[text()='{}']".format(text)) 

    def _find_elements_by_text(self, text):
        return self._browser.find_elements_by_xpath("//*[text()='{}']".format(text))