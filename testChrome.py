from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')
driver.maximize_window()
driver.get('https://www.facebook.com/')