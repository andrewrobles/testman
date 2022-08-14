from selenium import webdriver

from utils import InstagramBot
import configparser

from datetime import datetime

import json

file = open('settings.json', 'r')
settings = json.load(file)
file.close()

username = settings['username']
password = settings['password']

browser = webdriver.Firefox()
bot = InstagramBot(browser) 
bot.login(username, password)