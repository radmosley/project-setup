from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import csv
import time

#Open chrome and navigate to webpage
url = 'https://www.portlandoregon.gov/archives/'
print('url collected')

#Pass arguments to the Chrome Driver
options = Options()
prefs = {"download.default_directory" : "./code/downloads"}
options.add_experimental_option("prefs",prefs)
options.add_argument('--disable-dev-shm-usage')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.set_headless(headless=True)
options.binary_location = "/usr/bin/google-chrome-stable"
print('options collected')

#Initiate Driver
driver = webdriver.Chrome('/code/chromedriver', chrome_options= options)

print('driver created')

#Go to Bureau Landing page Transaction Search page
driver.get(url)

print('getting page')

def getLinks():
    internal_links = []
    external_links = []
    documents = []
    index = 0
    while index != internal_links:
        links = []
        savedLinks = []

        #check if page has a side section
        #if page has side section check if links have link text
        #if the link has link text and the link doesn't already exist in the savedlinks add link and text to savedLinks
        #if link does not have text pass to the next link
        #if no links exist pass to the next section
        if driver.find_element_by_id('section-nav'):
            try:
                section_nav = driver.find_element_by_id('section-nav')
                if section_nav.text is True:
                    links.append([section_nav.url, section_nav.text])
                else:
                    pass
            except:
                pass
        else:
            pass

        #check if page has a bureau section
        #if page has bureau section check if links have link text
        #if the link has link text and the link doesn't already exist in the savedlinks add link and text to savedLinks
        #if link does not have text pass to the next link
        #if no links exist pass to the next section
        if driver.find_element_by_id('bureau-nav'):
            try:
                bureau_nav = driver.find_element_by_id('bureau-nav')
                if section_nav.text is True:
                    links.append([bureau_nav.url, bureau_nav.text])
                else:
                    pass
            except:
                pass
        else:
            pass
        
        #check if page has a main-section
        #if page has main-section check if links have link text
        #if the link has link text and the link doesn't already exist in the savedLinks add link and text to savedLinks
        #if link does not have text add link to documents list and increase index and click next link
        if driver.find_element_by_tag_name('h1'):
            try:
                main_nav = driver.find_element_by_tag_name('h1')
                if main_nav.text is True:
                    links.append([main_nav, main_nav.text])
                else:
                    pass
            except:
                pass
        else:
            pass

        #for link in links if link base url is in link add link to internal links
        #if link does not have base url add link to external links
    print(internal_links)

getLinks()
