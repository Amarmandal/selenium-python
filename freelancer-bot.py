from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
import os

URL = 'https://www.freelancer.com/'

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver', options=chrome_options)
driver.maximize_window()
driver.get(URL)
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 50)
wait_2 = WebDriverWait(driver, 20)

assert "Hire Freelancers & Find Freelance Jobs Online | Freelancer" in driver.title

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'NavigationContainer')))

login_button = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-out-shell/app-navigation/app-navigation-logged-out/fl-bit/fl-container/fl-bit/fl-link[1]/a/div/div')
driver.execute_script("arguments[0].click(0);", login_button)


USERNAME = os.environ.get('FREELANCER_USERNAME')
PASSWORD = os.environ.get('FREELANCER_PASSWORD')

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "LoginPage")))

email_field = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/input')
email_field.send_keys(USERNAME)

password_field = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/input')
password_field.send_keys(PASSWORD)

submit_btn = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login/app-credentials-form/form/app-login-signup-button/fl-button/button')
submit_btn.click()

otp = getpass('Enter the opt sent to your mobile: ')

otp_field = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login/app-two-factor-form/form/fl-input/fl-bit/fl-bit/input')
otp_field.send_keys(otp)

verify_btn = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login/app-two-factor-form/form/app-login-signup-button/fl-button/button')
verify_btn.click()

hover_element = driver.find_element(By.XPATH, '/html/body/app-root/app-logged-in-shell/div/div[1]/div/app-navigation/app-navigation-primary/fl-bit/fl-container/fl-callout[1]/fl-callout-trigger/fl-button/button/fl-bit')

# hovering on the project
hover = ActionChains(driver).move_to_element(hover_element)
hover.perform()

projects = driver.find_element(By.XPATH, '//*[@id="cdk-overlay-0"]/div/fl-callout-content/div/div/app-browse/fl-bit/app-browse-links/fl-bit/fl-bit[2]/fl-grid/fl-col[1]/app-browse-links-item/fl-link/a')
driver.execute_script("arguments[0].click();", projects)

project_input = driver.find_element(By.XPATH, '//*[@id="search-results"]/fl-header-filter/div/div[1]/form/input')
project_input.send_keys('Nepali' + Keys.RETURN)

project_cards = driver.find_elements(By.CLASS_NAME, 'info-card-inner')
proj_card_price = driver.find_elements(By.CLASS_NAME, 'info-card-action')

print()
for proj in project_cards:
    proj_title = proj.find_element(By.CLASS_NAME, 'info-card-title')
    proj_description = proj.find_element(By.CLASS_NAME, 'info-card-description')
    print(proj_title.text)
    print()
    print(proj_description.text)
    print()

for price in proj_card_price:
    proj_price = price.find_element(By.CLASS_NAME, 'info-card-price')
    print(proj_price.text)
    print()



driver.close()