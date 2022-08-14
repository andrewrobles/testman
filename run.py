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

file = open('usernames.txt', 'r')
usernames = [line.strip() for line in file.readlines()]

browser = webdriver.Firefox()
bot = InstagramBot(browser) 
bot.login(username, password)