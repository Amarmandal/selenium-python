from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')
driver.get('https://modernwrites.com/login/')

ele = driver.find_element(By.ID, 'eael-user-login')
print(ele.is_displayed())
print(ele.is_enabled())

time.sleep(2)
remember_me = driver.find_element(By.CSS_SELECTOR, '//*[@id="rememberme"]')
print(remember_me.is_selected())
driver.quit()