from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Selenium Based Scrapper for PortlandOr'

    def handle(self, *args, **kwargs):
        #Open chrome and navigate to webpage
        url = 'https://www.portlandoregon.gov/archives/26978'
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
        delay = 3

        print('driver created')

        #Go to Bureau Landing page Transaction Search page
        driver.get(url)

        base_link = 'https://www.portlandoregon.gov/archives/'
        # def findLinks():
        #     content = driver.find_element_by_tag_name('body')
        #     bureaus = content.find_elements_by_tag_name('a')
        #     links = []
        #     ext_links = []
        #     for link in bureaus:
        #         if base_link in str(link.get_attribute('href')) and link not in links:
        #             links.append(link)
        #         elif link.get_attribute('href') == None:
        #             pass
        #         else:
        #             ext_links.append(link)
        
        # findLinks()
        
        # for a in links:
        #     a.click()
        #     findLinks()
        #// TODO: While page has links save links and click links
        #// TODO: If page has no links move to the next page
        #// TODO: Once a page has been search add it to the seen list
            
