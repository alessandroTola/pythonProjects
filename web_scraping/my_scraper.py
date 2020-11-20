#In this test I'd like populate some form fields, for instance subito.it web site interting the city in the serach bar
import scrapy
from scrapy.http import FormRequests


class WebScraper(scrapy.Spider): 
    name = "web_scraper"
    start_urls = ['https://www.subito.it']
    HTTPERROR_ALLOWED_CODES = [403]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    
    def start_requests(self):
        #urls = [f"https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?page={i}" for i in range(1,11)]
        urls = ['https://www.subito.it']
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        
        SET_SELECTOR = '.hp_narrow'
        for brickset in response.css(SET_SELECTOR):

            CATEGORIES_SELECTOR = 'h3 ::text'
            TITLE_ARTICLE_SELECTOR = './/div[@class="hp_thumb  "]/a/div/p/text()'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'

            yield {
                'name': brickset.css(CATEGORIES_SELECTOR).extract_first(),
                'article': brickset.xpath(TITLE_ARTICLE_SELECTOR).extract(),
            }
