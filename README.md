# Automation 2019

These files are automated test scripts for doing tasks using Selenium webdriver and Python.

## Getting started

The following scripts require Python and selenium webdriver. Pyhton is a scripting language used for many purposes from data science, object oriented programming, machine learning and many more.Selenium Webdriver is a third-party python module, which allows your script to access the internet and perform tasks automtically. Webdriver has a number of different versions, such as remote driver(for virtual machines), selenium grid (to do tests on multiple machines simultaneously), but we only need Chromedriver and Geckodriver for these scripts.

## Prerequisites
To run these scripts, first you will need to download Pyhton 3.7 or later from https://www.python.org/download/releases/3.0/

* Chromedriver is the webdriver for Google Chrome 
(http://chromedriver.chromium.org/downloads)

* GeckoDriver is the driver for all other browsers
(https://github.com/mozilla/geckodriver/releases)

You will need one or both of these for the scripts, depending on which tests or which browsers you want to use to test

Then you will need other Py dependencies, which I have listed here:
```
pip3 install selenium
pip3 install requests
pip3 install appium
```

To install these, you can open your terminal or command prompt and copy and paste them as they are.
*Notice the 3 next to pip. That means these dependencies will only work on pyhton 3.

You will also need to downoad the scripts from this repository. This can be done by downloading the zip file. (Git coming soon)

## Installing and running

When lanuching the script for the first time, make sure that the location of the driver or 'self.browser' in this case is the same as where you left your Chromedriver or Geckodriver. I leave mine as the downloads folder because that's where it will appear when I download something.

```
self.browser = webdriver.Chrome('/Users/yourName/Downloads/Chromedriver')
```
Launching from the terminal means you have to change your current directory to the location of the script. For eg. if your script is in the Downnloads folder. Try:
```
cd Downloads
```

the script can be launched from the terminal like using this simple python3 command (make sure you change the script.py to the name of the file you want to launch eg. python3 testAllLinks.py and if the file name has spaces use quotations like- python3 "test all links.py")

```
python3 script.py
```
or you can launch it using your IDE or text editor if it has python functionality.

### Headless or browser mode

Headless browser is a feature of selenium that allows a script to be run in the background of your machine instead of being able to see the script run, so it doesn't disrupt what you're doing. This is ideal if you are certain the script runs as intended and you are trying to do something that does not require your attention on the front such as grabbing data from a website or checking for certain attributes in the code. 

To turn headless on just make sure it is not commented out (has a hashtag infront) and to turn on headed, just add a hashtag ifront of the headless option. This applies to all options. In the example below, headless has been turned off so we can watch the script run.

```
#options.add_argument('--headless')
```

and almost like magic, we can turn headless mode back on.

```
options.add_argument('--headless')
```
### Changing target url

You can change the target url by pasting your desired url within the quotations.

```
url = ("https://www.website.com")
```

## Scripts in this repository

### Unfollow bot:
An instagram bot that goes through your most recently added friends and deletes them one by one, indiscriminately. 

### Like bot:
An instagram bot that goes through the top images of a chosen hashtag (from a list within python) and likes every image 

### Trello park:
A bot I made to save myself some time to input a new checklist of every park in London using selenium into a trello card

### Trello museum:
A bot I made to save myself some time to input a new checklist of every museum in London using selenium into a trello card

### Job search:
A timesaving script that opens up the top job sites and inputs a list item of your choice and location.

## Authors

* **Lee Davies** - *Initial work* - (https://github.com/LeethePerm)
