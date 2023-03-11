import os
from dotenv import load_dotenv
from pathlib import Path

# evn path and variables
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

SELENIUM_PATH=os.getenv("SELENIUM_PATH")
