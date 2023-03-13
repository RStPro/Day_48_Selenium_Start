import os
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
# we need to install webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# we also need to import By
from selenium.webdriver.common.by import By

# evn path and variables
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.es/-/pt/dp/B0B1YJRL9X/ref=sr_1_1?crid=2KC9ENME9RCD3&keywords=garmin+enduro+2&qid=1678548009&s=electronics&sprefix=garmin+enduro+%2Celectronics%2C97&sr=1-1')

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

# driver.close() # closes a tab
driver.quit() # quit the browser