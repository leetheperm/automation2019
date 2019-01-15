import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


email_list = ['lee', 'adam', 'bethany', 'nicole', 'silvia', 'gwen', 'bat', 'dog', 'cat', 'weasel', 'seal',]

email_prov = [ 'gmail.com', 'hotmail.com', 'protonmail.com', 'outlook.com',]

url = 'http://127.0.0.1:8080/'

agee = random.randint(15,98)

list_rand = random.choice(email_list)

num_rand = random.randint(0,999999999)

prov_rand = random.choice(email_prov)

emailer = (str(list_rand) + str(num_rand) + "@" + str(prov_rand))

class SandboxTest():


	def setUp(self):
		self.driver = webdriver.Chrome('/Users/Perm/Downloads/Chromedriver')
		self.driver.maximize_window()
		time.sleep(5)
		self.driver.get(url)
		time.sleep(5)

	def testSuite(self):

		driver = self.driver
		name = driver.find_element_by_xpath('//*[@id="field-email"]')
		name.click()
		time.sleep(1)
		name.send_keys(emailer)
		time.sleep(1)
		age_in = driver.find_element_by_xpath('//*[@id="field-age"]')
		age_in.click()
		time.sleep(.5)
		age_in.send_keys(agee)
		submiter = driver.find_element_by_xpath('//*[@id="form"]/button')
		submiter.click()
		time.sleep(3)
		close_el = driver.find_element_by_xpath('//*[@id="form-modal"]/div/div/div[1]/button')
		time.sleep(.5)
		# close_el.click()
		# time.sleep(3)

	def clearParameters(self):
		driver = self.driver
		name_clear = driver.find_element_by_xpath('//*[@id="field-email"]')
		name_clear.click()
		name_clear.clear()
		time.sleep(1)
		age_clear = driver.find_element_by_xpath('//*[@id="field-age"]')
		age_clear.click()
		time.sleep(.5)
		age_clear.clear()
		time.sleep(1)

	def tearDown(self):
		time.sleep(5)
		self.driver.quit()

	def stringCheckAge(self):
		driver = self.driver
		stringer = driver.find_element_by_xpath('//*[@id="form-data"]/tr[2]/td[1]')
		dave =stringer.text		
		if dave == ('Age in 30 years'):
			print('Test passed')
			print(dave)
		else:
			print('test failed')
			print(dave + " has an error")	

	def stringCheckEmail(self):
		driver = self.driver
		stringmail = driver.find_element_by_xpath('//*[@id="form-data"]/tr[1]/td[1]')
		mailcorrect = stringmail.text
		if mailcorrect == 'Email':
			print('test passed')
			print(mailcorrect)
		else:
			print('test failed')
			print(mailcorrect + ' has an error')			

lee = SandboxTest()
lee.setUp()
lee.testSuite()
lee.stringCheckEmail()
lee.stringCheckAge()
# time.sleep(10)
# lee.tearDown()




