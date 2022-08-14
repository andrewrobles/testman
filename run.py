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
message=settings['message']

file = open('usernames.txt', 'r')
usernames = [line.strip() for line in file.readlines()]

browser = webdriver.Firefox()
bot = InstagramBot(browser) 
bot.login(username, password)

is_first_message = True
for username in usernames:
    bot.send_message(username, message, is_first_message)
    is_first_message = False