### Program by Lee Davies. This script will open the Chrome browser, log into a trello account, choose a particular card and add a list item by item to that card 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

browser = webdriver.Chrome('/Users/Perm/Downloads/Chromedriver')

browser.get('http://www.trello.com')

time.sleep(2)

login =browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/a[1]')
login.click()

login_deets = browser.find_element_by_xpath('//*[@id="user"]')
login_deets.click()
login_deets.send_keys('Username')
password_deets = browser.find_element_by_xpath('//*[@id="password"]')
password_deets.click()
password_deets.send_keys('Password')
time.sleep(.5)
confirm_deets = browser.find_element_by_xpath('//*[@id="login"]')
confirm_deets.click()
time.sleep(2)

London = browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/ul/li[2]/a/div/div[1]')
London.click()
time.sleep(1)

park_card= browser.find_element_by_xpath('//*[@id="board"]/div[3]/div/div[2]/a/div[3]/span')
park_card.click()
time.sleep(2)


list_of_parks = ['Kenwood House ', 'Lamorbey Park ', 'Langtons Manor House Gardens ', 'Marble Hill Park ', 'Morden Hall Park ', 'Morden Park ', 'Osterley Park ', 'Syon House ', 'Valence House Museum ', 'Walpole Park', 'Kew Gardens ', 'London Wetland Centre', 'Phoenix Garden']

for item in list_of_parks:
	time.sleep(1)
	add_new_item = browser.find_element_by_xpath('//*[@id="classic"]/div[3]/div/div/div/div[5]/div[8]/div/div[4]/textarea')
	add_new_item.click()
	add_new_item.send_keys(item)
	time.sleep(1)
	add_again = browser.find_element_by_xpath('//*[@id="classic"]/div[3]/div/div/div/div[5]/div[8]/div/div[4]/div/input')
	add_again.click()
	time.sleep(1)
