from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time
import sys

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')

url = "https://www.brainyquote.com/"
driver.maximize_window()

#first tab
driver.get(url)
print(driver.current_url)
#second tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window('tab2')
driver.get('https://www.google.com/')

time.sleep(2)

driver.quit()

# first tab
# driver.get(url)

# #second tab
# driver.execute_script("window.open('about:blank', 'tab2');")
# driver.switch_to.window("tab2")
# driver.get('https://www.google.com')

# # third tab
# driver.execute_script("window.open('about:blank', 'tab3');")
# driver.switch_to.window('tab3')
# driver.get('https://www.facebook.com')

