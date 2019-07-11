from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class JobCrawler():

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome('/Users/Perm/Downloads/Chromedriver')

	def closeBrowser(self):
		self.driver.close()

	def linkedIn(self):
		browser = self.driver
		browser.get('https://www.linkedin.com')
		time.sleep(1)
		email = browser.find_element_by_xpath('//*[@id="login-email"]')
		email.click()
		time.sleep(1)
		email.send_keys(self.username)
		time.sleep(1)
		password = browser.find_element_by_xpath('//*[@id="login-password"]')
		password.click
		time.sleep(1)
		password.send_keys(self.password)
		time.sleep(1)
		logButton = browser.find_element_by_xpath('//*[@id="login-submit"]')
		logButton.click()
		time.sleep(2)
		searchBar = browser.find_element_by_xpath('//*[@id="ember32"]/input')
		searchBar.click()
		searchBar.send_keys(jobSearches)
		time.sleep(2)
		searchBar.send_keys(Keys.RETURN)

	# def newChromeTab(self):
	# 	self.driver.execute_script("window.open('new_window')")
	# 	time.sleep(1)
			
	
	def reed(self):
		browser = self.driver
		newie = browser.execute_script("window.open('https://www.reed.com','new window')")
		browser.switch_to.window(browser.window_handles[1])
		time.sleep(5)
		reedSearch = browser.find_element_by_xpath('//*[@id="main-keywords"]')
		reedSearch.click()
		reedSearch.send_keys(jobSearches)
		time.sleep(1)
		reedLocation = browser.find_element_by_xpath('//*[@id="main-location"]')
		reedLocation.click()
		time.sleep(.5)
		reedLocation.send_keys('London')
		reedLocation.send_keys(Keys.RETURN)



	def indeed(self):
		browser = self.driver
		mazu = browser.execute_script("window.open('new window')")
		time.sleep(1)
		browser.switch_to.window(browser.window_handles[2])
		browser.get('https://www.indeed.com/')
		time.sleep(2)
		indeedSearch = browser.find_element_by_xpath('//*[@id="text-input-what"]')
		indeedSearch.click()
		indeedSearch.send_keys(jobSearches)
		time.sleep(1)
		indeedConfirm = browser.find_element_by_xpath('//*[@id="whatWhere"]/form/div[3]/button')
		indeedConfirm.click()

	def cwJobs(self):
		browser = self.driver
		newnew = browser.execute_script("window.open('new window')")
		time.sleep(1)
		browser.switch_to.window(browser.window_handles[3])
		browser.get('https://www.cwjobs.co.uk/')
		time.sleep(2)
		cwSearch = browser.find_element_by_xpath('//*[@id="keywords"]')
		cwSearch.click()
		cwSearch.send_keys(jobSearches)
		time.sleep(1)
		cwLocate = browser.find_element_by_xpath('//*[@id="location"]')
		cwLocate.click()
		cwLocate.send_keys('London')
		cwLocate.send_keys(Keys.RETURN)

	def glassdoor(self):
		browser = self.driver
		newnew = browser.execute_script("window.open('new window')")
		time.sleep(1)
		browser.switch_to.window(browser.window_handles[4])
		browser.get('https://www.glassdoor.co.uk/')
		time.sleep(2)
		glassSearch = browser.find_element_by_xpath('//*[@id="KeywordSearch"]')
		glassSearch.click()
		glassSearch.send_keys(jobSearches)
		time.sleep(1)
		glassConfirm = browser.find_element_by_xpath('//*[@id="HeroSearchButton"]')
		glassConfirm.click()
		time.sleep(1)

	def google(self):
		browser = self.driver
		newnew = browser.execute_script("window.open('new window')")
		time.sleep(1)
		browser.switch_to.window(browser.window_handles[5])
		browser.get('https://www.google.co.uk/')
		time.sleep(2)
		googleSearch = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
		googleSearch.click()
		googleSearch.send_keys(jobSearches)
		googleSearch.send_keys(Keys.RETURN)



jobSearches = ['junior software tester']

# alternatives = 'QA tester' 'software tester' 'qa analyst' 'automation engineer' 'junior tester' 'junior QA'


searcher = JobCrawler('Username', 'Password',)
searcher.linkedIn()
time.sleep(2)
# searcher.newChromeTab()
# time.sleep(1)
searcher.reed()
time.sleep(2)
searcher.indeed()
time.sleep(2)
searcher.cwJobs()
time.sleep(1)
searcher.glassdoor()
searcher.google()
time.sleep(50)


