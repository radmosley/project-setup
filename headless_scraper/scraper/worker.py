from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import re
# import os


# display = 

#Open chrome and navigate to webpage
url = 'https://secure.sos.state.or.us/orestar/gotoPublicTransactionSearch.do'
driver = webdriver.Chrome()
driver.get(url)

#print website source code
# print(driver.page_source)

#Grab form and button elements
start = driver.find_element_by_id('cneSearchTranStartDate')
end = driver.find_element_by_id('cneSearchTranEndDate')
search_button = driver.find_element_by_name('search')

#Clear form input by default and input start and end dates
start.clear()
start.send_keys('01/01/2016')
end.clear()
end.send_keys('02/01/2016')

#click search button
search_button.click()

# print(start)
# print(end)
# print(search_button)

