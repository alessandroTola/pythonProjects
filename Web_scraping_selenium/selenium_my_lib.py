#Switch the package for the scraping, in this project I using selenium instead of scrapy
#Project: go to the github fill the research field with "python" print the title in the new page loaded
#python form_scraper.py https://github.com q python
#argv[1] wetsite
#argv[2] tab name -- for instance in the github file is "q"
#argv[2] search key
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

#web_site = sys.argv[1] if sys.argv[1] else "https://www.subito.it/"
#tab_name = sys.argv[2] if sys.argv[2] else "main-keyword-field"
#search_key = sys.argv[3] if sys.argv[3] else "Casa"

#web_site = "https://www.subito.it/"
web_site = 'https://www.subito.it/annunci-italia/vendita/usato/?q=casa&o=8782'
tab_name = "main-keyword-field"
search_key = "Casa"
oper_browser = True

#Setup browser configuration
def configure_chrome_browser(oper_browser, web_site):
    options = Options()
    options.headless = False if oper_browser else True
    options.add_argument("--window-size=1920,1200")

    DRIVER_PATH = '/Users/alessandrotola/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(web_site)

    return driver

