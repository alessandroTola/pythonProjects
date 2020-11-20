#Switch the package for the scraping, in this project I using selenium instead of scrapy
#Project: go to the github fill the research field with "python" print the title in the new page loaded
#python form_scraper.py https://github.com q python
#argv[1] betsite
#argv[2] tab name -- for instance in the github file is "q"
#argv[2] search key
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

#Setuo browser configuration
def configure_chrome_browser():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    DRIVER_PATH = './chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(sys.argv[1])

    return driver

driver = configure_chrome_browser()

field = driver.find_element_by_name(sys.argv[2])
field.send_keys(sys.argv[3])
field.submit();
title = driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[3]/div/div[1]/div/div[1]/h3")
print(title.text)

driver.quit()
