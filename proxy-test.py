from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep

PROXY = '182.52.90.42:51657'

# proxy = Proxy({
#     'proxType': ProxyType.MANUAL,
#     'httpProxy': PROXY,
#     'sslProxy': PROXY
# })

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('--proxy-server=%s' % PROXY)


driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver', options=chrome_options)
driver.maximize_window()

driver.get('https://httpbin.org/ip')
current_ip = driver.find_element(By.TAG_NAME, 'pre')
print(current_ip.text)
sleep(2)
driver.close()
