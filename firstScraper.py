from selenium import webdriver
import re
import csv

pattern = re.compile(r'https://2gis.ae/dubai/firm/\d*')

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')
driver.maximize_window()

url = 'https://2gis.ae/dubai/search/mobile%20shop'
driver.get(url)
# driver.implicitly_wait(10)

list_of_shops = driver.find_elements_by_class_name('_y3rccd')
list_of_links = []

for shop in list_of_shops:
    click_obj = shop.find_element_by_class_name('_1h3cgic')
    pp1 = click_obj.find_element_by_tag_name('a')
    pp2 = pp1.get_property('href')

    matches = pattern.findall(pp2)
    list_of_links.append(matches[0])


condition = True
my_raw_data = []
for link in list_of_links:
    driver.get(link)

    # accepting the browser cookies just once
    while condition:
        browser_cookies = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/footer/div[1]/div[2]/button')
        driver.execute_script("arguments[0].click()", browser_cookies)
        condition = False

    # click phone number
    my_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div/button')
    driver.execute_script("arguments[0].click();", my_btn)

    shop_name = driver.find_element_by_class_name('_oqoid')
    shop_address_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]')
    shop_address_2 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/span')
    shop_po_box = driver.find_element_by_class_name('_49kxlr')

    try:
        shop_po_box = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[6]/div[2]').text
    except:
        shop_po_box = "P.O Box is missing"  
    
    phone = driver.find_elements_by_class_name('_b0ke8')

    my_data = {
    "Name": shop_name.text.strip(),
    "Address": f'{shop_address_2.text}, {shop_address_1.text}',
    "P.O": shop_po_box.strip(),
    }

    # finding phone number
    phone_numbers = driver.find_elements_by_class_name('_b0ke8')

    for x in range(len(phone_numbers)):
        num = phone_numbers[x].find_element_by_tag_name('a')
        my_data[f"Phone-{x + 1}"] = num.find_element_by_tag_name('bdo').text.strip()


    my_raw_data.append(my_data)


with open('my_raw.csv', 'w', newline='') as f:
    field_names = ['Name', 'Address', 'P.O', 'Phone-1', 'Phone-2', 'Phone-3', 'Phone-4', 'Phone-5']
    file_writer = csv.DictWriter(f, fieldnames=field_names)

    file_writer.writeheader()
    for data in my_raw_data:
        file_writer.writerow(data)





