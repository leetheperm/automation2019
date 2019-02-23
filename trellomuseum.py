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

museum_card= browser.find_element_by_xpath('//*[@id="board"]/div[2]/div[1]/div[2]/a/div[3]/span')
museum_card.click()
time.sleep(2)



list_of_museums = ['British Library', 'British Museum', 'Geffrye Museum', 'Horniman Museum ', 'National Army Museum', 'National Gallery', 'National Portrait Gallery ', 'Natural History Museum ', 'Royal Air Force Museum ', 'Sir John Soanes Museum ', 'Wallace Collection', 'Imperial War Museums', 'Churchill War Rooms HMS Belfast Imperial War Museum London', 'Royal Museums Greenwich', 'Cutty Sark National Maritime Museum Queens House Royal Observatory', 'Science Museum Group', 'Science Museum', 'Tate', 'Tate Britain Tate Modern', 'Victoria and Albert Museum', 'V&A Museum of Childhood', 'Courtauld Gallery ', 'Dulwich Picture Gallery ', 'Hunterian Museum ', 'Jewish Museum ', 'Library and Museum of Freemasonry ', 'London Transport Museum ', 'Museum of Domestic Design and Architecture ', 'Petrie Museum of Egyptian Archaeology ', 'Royal Academy of Arts', 'Museum of London Docklands', 'Arsenal Football Club Museum ', 'Bank of England Museum ', 'Barbican Art Gallery ', 'Benjamin Franklin House ', 'Ben Uri Gallery ', 'Charles Dickens Museum ', "Dennis Severs' House ", 'Design Museum ', "Dr Johnson's House ", 'Estorick Collection of Modern Italian Art ', 'Fashion and Textile Museum ', 'Garden Museum ', 'Guildhall Art Gallery ', 'Hall Place Handel & Hendrix in London ', 'Hayward Gallery ', "Hogarth's House ", 'Institute of Contemporary Arts ', 'Leighton House Museum ', 'London Museum of Water & Steam ', 'Museum of Brands, Packaging and Advertising ', 'Museum of Immigration and Diversity ', 'Orleans House Gallery ', 'Postal Museum Royal ', 'Academy of Music Museum ', 'Saatchi Gallery ', 'Serpentine Galleries ', 'Sherlock Holmes Museum ', 'Two Temple Place ', 'Whitechapel Gallery ', 'William Morris Gallery', 'Florence Nightingale Museum ', 'Foundling Museum ', 'Freud Museum ', 'Museum of the Order of St John ', 'Old Operating Theatre ', 'Museum and Herb Garret Wellcome Collection', 'Barnet Museum ', 'Bruce Castle ', 'Burgh House ', 'Cuming Museum ', 'Forty Hall ', 'Greenwich Heritage Centre ', 'Gunnersbury Park ', 'Hackney Museum ', 'Harrow Museum ', 'Havering Museum ', 'Islington Museum ', 'Kingston Museum ', 'Museum of Croydon ', 'Museum of Richmond ', 'Museum of Wimbledon ', 'Twickenham Museum ', 'Valence House Museum ', 'Vestry House Museum ', 'Wandsworth Museum ', 'Whitehall Museum', "Queen's Gallery", 'Royal Mews', 'Banqueting House ', 'Whitehall ', 'Hampton Court Palace ', 'Kensington Palace ', 'Kew Palace ', 'Tower of London', '2 Willow Road ', '575 Wandsworth Road ', 'Blewcoat School ', "Carlyle's House ", 'Eastbury Manor House ', 'Fenton House ', 'George Inn ', 'Lindsey House ', 'Morden Hall Park ', 'Osterley Park ', 'Rainham Hall ', 'Red House ', 'Roman Baths ', 'Sutton House', 'Apsley House ', 'Chiswick House ', 'Down House ', 'Eltham Palace ', 'Jewel Tower ', 'Kenwood House', 'London Wall ', 'Marble Hill ', "House Ranger's House ", 'Winchester Palace']

for item in list_of_museums:
	time.sleep(1)
	add_new_item = browser.find_element_by_xpath('//*[@id="classic"]/div[3]/div/div/div/div[5]/div[8]/div/div[4]/textarea')
	add_new_item.click()
	add_new_item.send_keys(item)
	time.sleep(1)
	add_again = browser.find_element_by_xpath('//*[@id="classic"]/div[3]/div/div/div/div[5]/div[8]/div/div[4]/div/input')
	add_again.click()
	time.sleep(1)
