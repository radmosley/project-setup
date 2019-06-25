from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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

print('page loaded')

def getLinks():
    internal_links = []
    external_links = []
    index = 0
    #while index doesn't equal the total of internal links run the following function.
    #At the end of the function the index is increased by one to ensure all links that get collected are reviewed.
    # while index != len(internal_links)-1:
    #Test variable
    while index != 100:
        #Links contain all the a anchors referenced on the first page the driver is pointed to
        #For every link that on the current page if the link has an href then add that link to the saved links
        links = driver.find_elements_by_tag_name('a')
        savedLinks = []
        for link in links:
            if link.get_attribute('href'):
                savedLinks.append(link.get_attribute('href'))
 
        #For every link in the savedlinks section check if the link is an external or internal link,
        # check if the link already exist in one of the list and add it to the responding list
        for a in savedLinks:
            if a != None and url in a and a not in internal_links:
                internal_links.append(a)
            elif a != None and url not in a and a not in external_links:
                external_links.append(a)
        #While the app is running give me a check on if the links have been saved and how many links are in 
        # the responding list
        print('Internal Links Saved')
        print(len(internal_links))
        print('External Links Saved')
        print(len(external_links))
        driver.get(internal_links[index])
        print('Page {}'.format(internal_links[index]))
        #Move to the next item in the list
        index += 1
        #Prompt the user that the following link is being checked and wait 5 seconds before starting the process over again
        print('index = {}'.format(index))
        driver.implicitly_wait(5)
        #After the while loop is broken write the responding list to a csv file titled with the year month and day 
        # / hours and minutes the process was ran
    return [internal_links, external_links]
    

files = getLinks()

filename = time.strftime('%Y%m%d-%H%M')

internal = open('internal-{}.csv'.format(filename), 'w', newline='')
with internal:
    writer = csv.writer(internal, delimiter=',')
    writer.writerow(['Internal Links'])
    for item in files[0]:
        writer.writerows([files[0]])

external = open('external-{}.csv'.format(filename), 'w', newline='')
with external:
    writer = csv.writer(external, delimiter=',')
    writer.writerow(['External Links'])
    for item in files[1]:
        writer.writerow([item])

#// TODO: find a method that would check if an item is a document, webpage or external link


