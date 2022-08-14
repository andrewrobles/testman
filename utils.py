from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

class InstagramBot:
    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(60)
        self._base_url = 'https://www.instagram.com'
        self._browser.get(self._base_url)
        sleep(1)

    def login(self, username, password):
        username_input = self._browser.find_element_by_css_selector("input[name='username']")
        password_input = self._browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self._browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

    def search_username(self, username):
        self._browser.get('{}/direct/new'.format(self._base_url))
        sleep(1)

        search_input = self._browser.find_element_by_css_selector("input[placeholder='Search...']")
        search_input.send_keys(username)
        sleep(1)

    def send_message(self, username, message, is_first_message):
        self.search_username(username)
        
        if is_first_message == True:
            if len(self._find_elements_by_text('Turn on Notifications'))>0:
                turn_on_button=self._find_element_by_text('Not Now')
                turn_on_button.click()
                sleep(1)

        elements = self._find_elements_by_text(username)
        search_result = elements[-1]
        search_result.click()
        sleep(1)

        next_button = self._browser.find_element_by_xpath("//*[text()='{}']".format('Next'))
        next_button.click()
        sleep(3)

        message_input = self._browser.find_element_by_css_selector("textarea[placeholder='Message...']")
        message_input.send_keys(message)
        message_input.send_keys(Keys.ENTER)
        sleep(1)      

    def search_hashtag(self, hashtag):
        self._browser.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag[1:]))
        sleep(1)

    def get_hrefs(self, hashtag):
        self.search_hashtag(hashtag)

        html = self._browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        return [a['href'] for a in soup.find_all('a')]

    def get_usernames_by_hashtag(self, hashtag):
        first_href = self.get_hrefs(hashtag)[0]
        self._browser.get('https://www.instagram.com{}'.format(first_href))

        likes_href = '{}{}'.format(first_href, 'liked_by/')
        likes_tag = self._browser.find_element_by_xpath('//a[@href="{}"]'.format(likes_href))
        likes_tag.click()
        sleep(1)

        soup = BeautifulSoup(self._browser.page_source, 'html.parser')
        return [element['href'][1][-1] for element in soup.find_all('a', {'class': '_2dbep qNELH kIKUG'})] 


    def _find_element_by_text(self, text):
        return self._browser.find_element_by_xpath("//*[text()='{}']".format(text)) 

    def _find_elements_by_text(self, text):
        return self._browser.find_elements_by_xpath("//*[text()='{}']".format(text))