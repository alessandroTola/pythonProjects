#Primo esperimento, recuperare tutti i titoli degli articoli presenti delle diverse categorie all'interno della homepage
import scrapy


class WebScraper(scrapy.Spider): 
    name = "web_scraper"
    start_urls = ['https://www.wikihow.it/Pagina-principale']
    HTTPERROR_ALLOWED_CODES = [403]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    

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
