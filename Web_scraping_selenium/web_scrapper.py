from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class WebScrapper():
    
    __driver = []
    
    def __init__(self, web_site, driver_path):
        self.__web_site = web_site
        self.__driver_path = driver_path
        
        
    def configure_chrome_browser(self, open_windows_driver):
        options = Options()
        options.headless = open_windows_driver 
        options.add_argument("--window-size=1920,1200")
        self.__driver = webdriver.Chrome(options=options, executable_path=self.__driver_path)
        self.__driver.get(self.__web_site)

    def search_items_form(self, search_name, search_key, search_button_id, items_class, item_name, search_button_exist):
        self.__driver.implicitly_wait(3)
        try:
            search_field = self.__driver.find_element_by_name(search_name)
            search_field.send_keys(search_key)
            search_field.send_keys(Keys.RETURN);
            if(search_button_exist):
                search_button = self.__driver.find_element_by_class_name(search_button_id)
                search_button.click()
            print("Research done")
        except:
            print("Search field does not exist")
        
        try:
            items = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, items_class))
            )
            print("Element found")
            elements = items.find_elements_by_class_name(item_name)
            
            return elements
        except:
            print("No elements with this tag")
            
    #Method for finding link by name
    def navigate_link_by_text(self, link_name):        
        try:
            link = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, link_name))
            )
            print("Link found")
            link.click()
        except:
            print("No link found")
            
    #Method for finding and navigate a list of pages (subito.it)
    def next_page(self, next_button_xpath):
        try:
            link = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, next_button_xpath))
            )
            link.click()
            print("Next page")
        except:
            print("No other pages")
            