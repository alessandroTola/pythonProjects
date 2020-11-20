#In this scraper I'd like to fill some form with python script, for instance a real estate agneziy
#I choose immobiliare.it for my experimets, I fill a location form and save the result in a json file
import scrapy
from scrapy_splash import SplashRequest

class WebScraper(scrapy.Spider): 
    name = "web_scraper"
    start_urls = ['https://www.subito.it/']
    HTTPERROR_ALLOWED_CODES = [403]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    
    def parse(self, response):
        formdata = {"q": "oristano"}
        yield SplashRequest(
            response,
            url=self.start_urls, 
            formdata=formdata,
            callback=self.print_response
            )

    def print_response(self, response):
        print(response.status)
