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
from web_scrapper import WebScrapper


#Method for saving e loading data to/from json
def save_json_data(data_path, data):
    with open(data_path, 'w') as outfile:
        json.dump(data, outfile)
        
def load_from_json(data_path, data):
    with open(data_path) as json_file:
        data = json.load(json_file)
        
    for p in data['articles']:
        print('title: ' + p['title'])
        print('price: ' + p['price'])
        print('src_image: ' + p['src_image'])
        print('')
        
def get_data_from_elements(data, elements):
    data['articles'] = []
    for element in elements:
        title = element.find_element_by_tag_name('h2').text
        try:          
            price = element.find_element_by_tag_name('h6').text.split(" ")[0]           
        except:
            price = 'NP'
        
        try:
            image_src = element.find_element_by_tag_name('img').get_attribute("src") 
        except:
            image_src = 'NP'
            
        data['articles'].append({
                'title' : title,
                'price' : price,
                'src_image' : image_src
            })
        
        
web_site = "https://www.subito.it/"
#web_site = 'https://www.subito.it/annunci-italia/vendita/usato/?q=casa&o=8782'
data_path = '/Users/alessandrotola/OneDrive - Università di Cagliari/Projects/Web_scraping_selenium/data.txt'
DRIVER_PATH = '/Users/alessandrotola/chromedriver'
tab_name = "main-keyword-field"
search_key = "Casa"
search_button_id = 'button-icon-lens'
items_class = 'jsx-59941399.items.visible'
item_name = 'jsx-3924372161.items__item'
data = {}
open_browser = True

scraper = WebScrapper(web_site, DRIVER_PATH)
scraper.configure_chrome_browser(True)
element = scraper.search_items_form(tab_name, search_key, search_button_id, items_class, item_name, True)
get_data_from_elements(data, element)
save_json_data(data_path, data)

#Cofigurare driver    
#driver = configure_chrome_browser()

#Setup browser configuration
def configure_chrome_browser():
    options = Options()
    options.headless = False if open_browser else True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(web_site)

    return driver

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
            try:
                price = element.find_element_by_tag_name('h6').text.split(" ")[0]
            except:
                price = "NP"
            #image_src = element.find_element_by_tag_name('img').get_attribute("src")
            print(title.text)
            print(price)
            data['articles'].append({
                'title' : title.text,
                'price' : price
                #'src_image' : image_src
            })
    except:
        print("No elements with this tag")
        driver.quit()
        
#Method for finding link by name
def navigate_link_by_text(link_name):        
    try:
        link = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_name))
        )
        print("Link found")
        link.click()
    except:
        print("No link found")
        
#search_item_form(driver)
#save_json_data()           
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
#driver.quit()