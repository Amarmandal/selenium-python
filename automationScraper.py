from selenium import webdriver
import pandas as pd
import re
import csv

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')
driver.maximize_window()

URL = 'https://webscraper.io/test-sites/e-commerce/allinone'
driver.get(URL)

click_obj = driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a')
click_obj.click()

laptop_obj = driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a')
laptop_obj.click()

list_of_products = driver.find_elements_by_class_name('thumbnail')

list_of_links = []
for item in list_of_products:
    just_link = item.find_elements_by_tag_name('h4')[-1]
    pp1 = just_link.find_element_by_tag_name('a')
    pp2 = pp1.get_property('href')

    list_of_links.append(pp2)

list_of_item = []
for x in range(5):
    driver.get(list_of_links[x])
    product_name = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]')
    product_price = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]')
    product_review = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p')

    my_item = {
        "Product Name": product_name.text.strip(),
        "Product Price": product_price.text.strip(),
        "Rating": product_review.text.strip()
    }

    list_of_item.append(my_item)

df = pd.DataFrame(list_of_item)
print(df)