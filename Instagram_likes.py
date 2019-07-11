""" Tutorial by Markets and data (https://www.youtube.com/channel/UCtGNWBSiriWivCbuPX4M_Wg)

Program adjusted by Lee Davies based on above tutorial. """


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import sys

keys = Keys()

class InstagramBot:
	def __init__(self, username, password, ):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/")		
		time.sleep(.5)
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
		time.sleep(2)
		
	def like_photo(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
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
		            time.sleep(.5)
		    except Exception as e:
		        time.sleep(1)
		    unique_photos -= 1
		    # <button class="oW_lN _0mzm- sqdOP yWX7d        " type="button">Follow</button>
		    #/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button
		    #/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button


Lee = InstagramBot("Username", "Password")
Lee.login()

hashtag = ['london', 'christmas', 'roadtrip', 'babes', 'boobs', 'happy','streetfood', 'traveller' 'travel', 'citylife' 'destination', 'curry', 'sporty', 'nike'
		 'urban','street', 'UK', 'Europe', 'architecture', 'vegan', 'England', 'English', 'Britain', 'citytour' ]
while True:
        # Choose a random tag from the list of tags
	tag = random.choice(hashtag)
	Lee.like_photo(tag)
	Lee.closeBrowser()
	time.sleep(60)
	Lee = InstagramBot(username, password)
	Lee.login()
