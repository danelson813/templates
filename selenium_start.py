from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_driver(url):
    firefox_driver_path = "/Users/dannelson/geckodriver"
    service = Service(firefox_driver_path)

    driver = webdriver.Firefox(service=service)
    browser = driver
    driver.get(url)
    print(driver.title)
    browser = driver
   
    driver.close()
    return browser

if __name__ == "__main__":
    browser = get_driver('https://google.com')
    print(type(browser))