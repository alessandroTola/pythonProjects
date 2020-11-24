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
import json

#web_site = sys.argv[1] if sys.argv[1] else "https://www.subito.it/"
#tab_name = sys.argv[2] if sys.argv[2] else "main-keyword-field"
#search_key = sys.argv[3] if sys.argv[3] else "Casa"

web_site = "https://www.subito.it/"
#web_site = 'https://www.subito.it/annunci-italia/vendita/usato/?q=casa&o=8782'
tab_name = "main-keyword-field"
search_key = "Casa"
open_browser = True
data_path = '/Users/alessandrotola/OneDrive - Università di Cagliari/Projects/Web_scraping_selenium/data.txt'
data = {}

#Setup browser configuration
def configure_chrome_browser():
    options = Options()
    options.headless = False if open_browser else True
    options.add_argument("--window-size=1920,1200")

    DRIVER_PATH = '/Users/alessandrotola/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(web_site)

    return driver
#Method for saving data from scraping
def save_json_data():
    with open(data_path, 'w') as outfile:
    json.dump(data, outfile)
    
driver = configure_chrome_browser()

#Given a tag name and search key we can do a research in the serch bar, and print the titles of the items
def search_item_form(driver):
    search_field = driver.find_element_by_name(tab_name)
    search_field.send_keys(search_key)
    search_field.send_keys(Keys.RETURN);
    search_button = driver.find_element_by_class_name('button-icon-lens')
    search_button.click()
    print("Element found")
    
    try:
        items = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-59941399.items.visible"))
        )
        elements = items.find_elements_by_class_name('jsx-3924372161.items__item')
        data['articles'] = []
        for element in elements:
            title = element.find_element_by_tag_name('h2')
            #price = element.find_element_by_tag_name('h6')
            #image_src = element.find_element_by_tag_name('img').get_attribute("src")
            print(title.text)
            data['articles'].append({
                'title' : title.text,
                #'price' : int(price.text),
                #'src_image' : image_src
            })
    except:
        print("No elements with this tag")
        driver.quit()

search_item_form(driver)

#Method for finding link by name
def navigate_link_by_text(driver):        
    try:
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Inserisci annuncio"))
        )
        print("Link found")
        link.click()
    except:
        print("No link found")
        driver.quit()
            
#navigate_link_by_text(driver)

#Method for finding and navigate a list of pages (subito.it)
def next_page(driver):
    try:
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='layout']/main/div[2]/div[5]/div[2]/div[3]/a[2]"))
        )
        link.click()
        print("Next page")
    except:
        print("No other pages")

#next_page(driver)
time.wait(5)
driver.quit()
