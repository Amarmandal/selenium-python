from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')

driver.get('https://modernwrites.com/')
print(driver.title)

driver.get('https://consultmanish.com/')
print(driver.title)

driver.back() #back navigation 
print(driver.title)

driver.forward() #forward navigation
print(driver.title)