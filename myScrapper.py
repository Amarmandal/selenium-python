# import requests
# from bs4 import BeautifulSoup

# URL = "https://2gis.ae/dubai/search/mobile%20shop"
# page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find_all('div', class_="_y3rccd")

# results = soup.find(id='ResultsContainer')
# job_elems = results.find_all('section', class_='card-content')


# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()

# for ele in results:
#     shop_name = ele.find('span', {"class": "_hc69qa"})
#     shop_address = ele.find('span', {"class": "_tluih8"})
#     shop_number = ele.find('bdo', {"bdo": "ltr"})
#     print(shop_name.text.strip())
#     print(shop_address.text.strip())
#     print(shop_number.text.strip())

from selenium import webdriver

url = "https://www.youtube.com/c/technicalview/videos?view=0&sort=p&flow=grid"

driver = webdriver.Chrome()

driver.get(url)
