import os
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# evn path and variables
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

# we need to install webdriver-manager
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.amazon.es/pt')