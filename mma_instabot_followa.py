""" Tutorial by Markets and data (https://www.youtube.com/channel/UCtGNWBSiriWivCbuPX4M_Wg)

Program adjusted by Lee Davies based on above tutorial. """


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time
import sys

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')


keys = Keys()

class InstagramBot:
	def __init__(self, username, password,):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome(executable_path='/Users/Perm/Downloads/Chromedriver')

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/")
		driver.get_screenshot_as_file("insta.png")	
		print("Headless Chrome Initialized")	
		time.sleep(2)
		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(2)
		user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
		passworword_elem.clear()
		passworword_elem.send_keys(self.password)
		passworword_elem.send_keys(Keys.RETURN)
		driver.get_screenshot_as_file("post.png")
		time.sleep(2)
		
	def like_photo(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		driver.get_screenshot_as_file("likes.png")
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
			follow = lamba : driver.find_element_by_class_name('oW_lN _0mzm- sqdOP yWX7d')	
	        follow.click()
	        print("following")
	        for second in reversed(range(0, random.randint(18, 28))):
	            print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
	                            + " | Sleeping " + str(second))
	            driver.get_screenshot_as_file("gua.png")
	            time.sleep(.5)


Lee = InstagramBot("mma.slam", "Iamweasel1")
Lee.login()

hashtag = ['UFC', 'fight', 'mma', 'mma-fighting', 'UFCLondon', 'UFC241','UFC237', 'UFC238', 'UFC239', 'UFCfightnight', 'bjj', 'muaythai', 'bellator', 'cagewarriors']
while True:
        # Choose a random tag from the list of tags
	tag = random.choice(hashtag)
	Lee.like_photo(tag)

	# Lee.closeBrowser()
	time.sleep(1)
	# Lee = InstagramBot(username, password)
	# Lee.login()