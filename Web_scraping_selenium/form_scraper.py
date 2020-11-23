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

web_site = "https://www.subito.it/"
tab_name = "main-keyword-field"
search_key = "Casa"

#Setuo browser configuration
def configure_chrome_browser():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    DRIVER_PATH = '/Users/alessandrotola/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(web_site)

    return driver

driver = configure_chrome_browser()

def search_item_form(driver):
    search_field = driver.find_element_by_name(tab_name)
    search_field.send_keys(search_key)
    search_field.send_keys(Keys.RETURN);
    search_button = driver.find_element_by_class_name('button-icon-lens')
    search_button.click()

    try:
        items = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-59941399.items.visible"))
        )
        elements = items.find_elements_by_class_name('jsx-3924372161.items__item')
        for element in elements:
            title = element.find_element_by_tag_name('h2')
            print(title.text)
        print("Element found")
        
    finally:
        print("No elements with this tag")
        driver.quit()

search_item_form(driver)
#driver.quit()
