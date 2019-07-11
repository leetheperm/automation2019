
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import sys

class InstagramBot:
	def __init__(self, username, password, ):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome('/Users/Perm/Downloads/Chromedriver')

	def closeBrowser(self):
		self.driver.close()
		# basic login stuff
	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/")		
		time.sleep(1)
		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(1)
		user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
		passworword_elem.clear()
		passworword_elem.send_keys(self.password)
		passworword_elem.send_keys(Keys.RETURN)
		time.sleep(4)

	# def notNow(self):
			
	#this part will find a list of your followers and delete the top follower, then refresh and do it again while the loop is on
	def findFollowing(self):
		driver = self.driver
		mylink = driver.get('https://www.instagram.com/londonian_art/')
		time.sleep(2)
		myprofile = driver.find_element_by_partial_link_text("following")
		time.sleep(1)
		myprofile.click()
		time.sleep(2)
		followerList = driver.find_element_by_css_selector("div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl")
		followerList.click()
		time.sleep(1)
		unfollowEach = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[1]")
		unfollowEach.click()
		time.sleep(1)
		



gram = InstagramBot("username", "password")
gram.login()
#change the number below for how many subscribers you want to delete. Sometimes anything over 10 is caught by Instagrams bot detector and will stop unfollowing
for i in range(50):		
	gram.findFollowing()
gram.closeBrowser()
