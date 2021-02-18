from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass
import selenium.webdriver.support.expected_conditions as EC
import time

PASSWORD = getpass('Enter your password: ')

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')
driver.maximize_window()

url = 'https://meroshare.cdsc.com.np/#/login'
driver.get(url)

assert "Mero Share" in driver.title

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "login-container")))

def handle_dp():
    dp_field = driver.find_element_by_id('selectBranch')
    dp_field.click()

    dp_input = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    dp_input.send_keys("10600" + Keys.RETURN)



def handle_input_box():
    user_input = driver.find_element_by_id('username')
    user_pass = driver.find_element_by_id('password')

    USERNAME = getpass("Enter your DP Id:")

    user_input.send_keys(USERNAME)
    user_pass.send_keys(PASSWORD)


handle_dp()
handle_input_box()

sign_in = driver.find_element_by_xpath('/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button')
sign_in.click()

