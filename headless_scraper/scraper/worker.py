from selenium import webdriver

def docPull():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    print("page loaded")


docPull()