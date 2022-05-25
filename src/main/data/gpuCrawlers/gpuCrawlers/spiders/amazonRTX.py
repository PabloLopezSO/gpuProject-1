import scrapy
from ..items import GpucrawlersItem
from datetime import date
from scrapy.loader import ItemLoader

test = date.today()
class AmazonrtxSpider(scrapy.Spider):
    name:str = 'amazonRTX'
    pageNumber:int = 2
    start_urls:str = ['https://www.amazon.com/s?k=rtx+series+3000+gpu&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1XWXLKRZAXVCP&sprefix=rtx+series+3000+gpu%2Caps%2C108&ref=nb_sb_noss']


    def parse(self, response):
        products:str = response.css('.s-list-col-right > .sg-col-inner')
        for product in products:
            itemsLoader = ItemLoader(item = GpucrawlersItem(), selector=product)
            itemsLoader.add_css('productName', '.a-color-base.a-text-normal::text')
            itemsLoader.add_css('productPrice', '.a-price-whole::text')
            itemsLoader.add_value('productDate', date.today())
            yield itemsLoader.load_item()

            nextPage:str = f'https://www.amazon.com/s?k=rtx+series+3000+gpu&page={AmazonrtxSpider.pageNumber}&crid=1MM80MTZ9VL0Q&qid=1644680443&sprefix=rtx+series+3000+gpu%2Caps%2C116&ref=sr_pg_{AmazonrtxSpider.pageNumber}'
            if AmazonrtxSpider.pageNumber  <= 7:
               AmazonrtxSpider.pageNumber += 1
            yield response.follow(nextPage, callback = self.parse)
