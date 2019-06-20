from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv
from lxml import html
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

print('page loaded')





# def getLinks():
#     internal_links = []
#     external_links = []
#     collected = []
#     index = 0
#     # while index != len(internal_links)-1:
#     # browser = driver.page_source
#     links = driver.cssselect('a')
#     for link in links:
#         if 'href' in link.attrib:
#             collected.append(link.attrib['href'])
#     print(collected)

# getLinks()

def getLinks():
    internal_links = []
    external_links = []
    index = 0
    # while index != len(internal_links)-1:
    while index != 1000:
        links = driver.find_elements_by_tag_name('a')
        savedLinks = []
        for link in links:
            if link.get_attribute('href'):
                savedLinks.append(link.get_attribute('href'))
        # print(savedLinks)
        for a in savedLinks:
            if a != None and url in a and a not in internal_links:
                internal_links.append(a)
            elif a != None and url not in a and a not in external_links:
                external_links.append(a)
        print('Internal Links Saved')
        print(len(internal_links))
        print('External Links Saved')
        print(len(external_links))
        driver.get(internal_links[index])
        print('Page {}'.format(internal_links[index]))
        index += 100
        print('index = {}'.format(index))
        driver.implicitly_wait(5)
    
    filename = time.strftime('%Y%m%d-%H%M%S')
    myFile = open('{}.csv'.format(filename), 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(['Internal Links', 'External Links'])
        writer.writerows({
            'Internal Links': internal_links,
            'External Links': external_links
        })

getLinks()
#// TODO: Get initial set of links
#// TODO: After initial list is generated continue process using the savedLink list.


