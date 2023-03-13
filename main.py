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

driver.get('https://www.garmin.com/pt-PT/p/854515')
Xpath = '//*[@id="js__product__info__name"]'
price = driver.find_element(By.XPATH, Xpath).get_attribute("innerHTML")

print(price)

# driver.close() # closes a tab
driver.quit() # quit the browser
