#Codice preso da: https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
#semplice scraper per prendere alcuni dati come imagini, numero pezzi ecc dal sito: https://brickset.com/

import scrapy


class WebScraper(scrapy.Spider): #Spyder ha tutti i metodi e cose utili per analizzare le pagine
    name = "web_scraper"
    start_urls = ['http://brickset.com/sets/year-2016'] #Lista dei siti da scraperare
    HTTPERROR_ALLOWED_CODES = [403]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    

    def parse(self, response):
        
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 ::text'
            #This selector cames from HTML sniper 1
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces' : brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs' : brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image' : brickset.css(IMAGE_SELECTOR).extract_first(), 
            }

            #This selector cames from HTML sniper 1
            NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page), 
                    callback=self.parse
                )


#HTML code sniper 1
#<article class="set">
#  <a class="highslide plain mainimg" href="http://images.brickset.com/sets/images/10251-1.jpg?201510121127" onclick="return hs.expand(this)">
#    <img src="http://images.brickset.com/sets/small/10251-1.jpg?201510121127" title="10251-1: Brick Bank"></a>
#  ...
#  <div class="meta">
#    <h1><a href="/sets/10251-1/Brick-Bank"><span>10251:</span> Brick Bank</a> </h1>
#    ...
#    <div class="col">
#      <dl>
#        <dt>Pieces</dt>
#        <dd><a class="plain" href="/inventories/10251-1">2380</a></dd>
#        <dt>Minifigs</dt>
#        <dd><a class="plain" href="/minifigs/inset-10251-1">5</a></dd>
#        ...
#      </dl>
#    </div>
#    ...
#  </div>
#</article>

#HTML sniper 2
#<ul class="pagelength">
#
#  ...
#
#  <li class="next">
#    <a href="http://brickset.com/sets/year-2017/page-2">&#8250;</a>
#  </li>
#  <li class="last">
#    <a href="http://brickset.com/sets/year-2016/page-32">&#187;</a>
#  </li>
#</ul>