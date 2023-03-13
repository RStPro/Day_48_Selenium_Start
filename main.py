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
Xpath = '//*[@id="js__product__price__main"]/span[1]'
price = driver.find_element(By.XPATH, Xpath).get_attribute("innerHTML") # getting innerHTML to have the span text
price_text = str((price).replace('&nbsp;', "")) # replacing white space by '' and converting to stirng
price_number = float(price_text.replace(',', '.')) # replacing the ',' by '.' and convert to float
print(price_number)

# driver.close() # closes a tab
driver.quit() # quit the browser
