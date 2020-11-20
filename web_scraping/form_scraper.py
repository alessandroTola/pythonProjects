#In this test I'd like populate some form fields, for instance subito.it web site interting the city in the serach bar
import scrapy


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

    def parse(self,response):
        form_data = {'q':'case'}
        return scrapy.FormRequest.from_response(
                            response, 
                            formdata = form_data 
        )
