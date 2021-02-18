from selenium import webdriver
import re
import csv

# pattern = re.compile(r'https://2gis.ae/dubai/firm/\d*')

driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver')
driver.maximize_window()


url = 'https://2gis.ae/dubai/firm/70000001028768375'
driver.get(url)
driver.implicitly_wait(10)

browser_cookies = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/footer/div[1]/div[2]/button')
driver.execute_script("arguments[0].click()", browser_cookies)


my_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div/button')
driver.execute_script("arguments[0].click();", my_btn)

shop_name = driver.find_element_by_class_name('_oqoid')
shop_address_1 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]')
shop_address_2 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/span')
try:
    shop_po_box = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[6]/div[2]').text
except:
    shop_po_box = "P.O Box is missing"    
   

my_data = {
    "Name": shop_name.text.strip(),
    "Address": f'{shop_address_2.text}, {shop_address_1.text}',
    "P.O": shop_po_box.strip(),
    }

phone_numbers = driver.find_elements_by_class_name('_b0ke8')

for x in range(len(phone_numbers)):
    num = phone_numbers[x].find_element_by_tag_name('a')
    my_data[f"Phone-{x + 1}"] = num.find_element_by_tag_name('bdo').text.strip()
    
# new_list = []
# new_list.append(my_data)


with open('my_raw.csv', 'w', newline='') as f:
    field_names = ['Name', 'Address', 'P.O', 'Phone-1', 'Phone-2', 'Phone-3']
    file_writer = csv.DictWriter(f, fieldnames=field_names)

    file_writer.writeheader()
    file_writer.writerow(my_data)
# df = pd.DataFrame(new_list)
# print(df)





