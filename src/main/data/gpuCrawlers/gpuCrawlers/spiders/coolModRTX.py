import scrapy
from ..linkExtractor import urlExctractor
from ..items import GpucrawlersItem
from scrapy.loader import ItemLoader
from datetime import date

class CoolmodrtxSpider(scrapy.Spider):
    name:str = 'coolModRTX'
    start_urls = urlExctractor()
    
    def parse(self, response):
        products:str = response.css('.row')
        itemsLoader = ItemLoader(item = GpucrawlersItem(), selector=products)
        itemsLoader.add_css('productName', '.productTitle::text')
        itemsLoader.add_css('productPrice', '#normalpricenumber::text')
        itemsLoader.add_value('productDate', date.today())
        yield itemsLoader.load_item()