#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time
import sys
import datetime

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')


keys = Keys()
x = datetime.datetime.now()
class InstagramBot:
	def __init__(self, username, password,):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome(options = options, executable_path='/Users/Perm/Downloads/Chromedriver')

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/")
		driver.get_screenshot_as_file("insta.png")	
		print("Headless Chrome Initialized")
		print(x.strftime("%d-%B-%H:%M"))
		time.sleep(2)
		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(.5)
		user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
		passworword_elem.clear()
		passworword_elem.send_keys(self.password)
		passworword_elem.send_keys(Keys.RETURN)
		driver.get_screenshot_as_file("post.png")
		print('logged in')
		time.sleep(2)
		
	def like_photo(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		driver.get_screenshot_as_file("likes.png")
		print('liking')
		time.sleep(.1)

		pic_hrefs = []
		for i in range(1, 7):
		    try:
		        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		        time.sleep(1)
		        # get tags
		        hrefs_in_view = driver.find_elements_by_tag_name('a')
		        # finding relevant hrefs
		        hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
		                         if '.com/p/' in elem.get_attribute('href')]
		        # building list of unique photos
		        [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
		        # print("Check: pic href length " + str(len(pic_hrefs)))
		    except Exception:
		        continue

		unique_photos = len(pic_hrefs)
		for pic_href in pic_hrefs:
		    driver.get(pic_href)
		    time.sleep(1)
		    try:
		        time.sleep(random.randint(1, 2))
		        like_button = lambda: driver.find_element_by_xpath("//*[@aria-label='Like']").click()
		        like_button().click()
		        for second in reversed(range(0, random.randint(18, 28))):
		            print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
		                            + " | Sleeping " + str(second))
		            driver.get_screenshot_as_file("gua.png")
		            time.sleep(.5)
		    except Exception as e:
		        time.sleep(1)
		    unique_photos -= 1
		    # <button class="oW_lN _0mzm- sqdOP yWX7d        " type="button">Follow</button>
		    #/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button
		    #/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button


Lee = InstagramBot("bobbycoot", "Iamweasel1")
Lee.login()

hashtag = ['UFC', 'fight', 'mma', 'mma-fighting', 'UFCLondon', 'UFC241','UFC237', 'UFC238', 'UFC239', 'UFCfightnight', 'bjj', 'muaythai', 'bellator', 'cagewarriors']
for i in range(30):
        # Choose a random tag from the list of tags
	tag = random.choice(hashtag)
	Lee.like_photo(tag)
	# Lee.closeBrowser()
	time.sleep(1)
	# Lee = InstagramBot(username, password)
	# Lee.login()