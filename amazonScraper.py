from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import csv

URL = 'https://www.amazon.in/'

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver', options=options)
driver.maximize_window()
driver.get(URL)
driver.implicitly_wait(10)

search_query = 'Samsung Phones'

if(len(sys.argv) >= 2):
    search_query = sys.argv[1]

input_box = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
input_box.send_keys(search_query + Keys.RETURN)

samsung_check_box = driver.find_element_by_xpath('//*[@id="p_89/Samsung"]/span/a/span')
samsung_check_box.click()

phones = driver.find_elements(By.XPATH, '//*[@class="a-size-medium a-color-base a-text-normal"]')
prices = driver.find_elements(By.CLASS_NAME, 'a-price-whole')

scraped_data = []

if(len(phones) == len(prices)):
    for x in range(len(phones) -1):
        data = {
            "Phone Name": phones[x].text,
            "Price": prices[x].text
        }

        scraped_data.append(data)


with open('amazon-data.csv', 'w', newline='') as f:
    field_names = []
    for key in scraped_data[0].keys():
        field_names.append(key)
    
    file_writer = csv.DictWriter(f, fieldnames=field_names)
    file_writer.writeheader()
    for data in scraped_data:
        file_writer.writerow(data)