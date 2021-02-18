from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep

PROXY = '182.52.90.42:51657'

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument(f'--proxy-server={PROXY}')


driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver', options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    driver.get('https://httpbin.org/ip')
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    current_ip = driver.find_element(By.TAG_NAME, 'pre')
    print(current_ip.text)
except TimeoutException as ex:
    print(ex)
finally:
    sleep(2)
    driver.close()




