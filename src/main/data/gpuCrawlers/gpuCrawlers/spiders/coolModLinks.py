import scrapy
from ..items import GpucrawlersItem

class CoolmodlinksSpider(scrapy.Spider):
    name:str = 'coolModLinks'
    start_urls:str = ['https://www.coolmod.com/tarjetas-graficas/']
    
    def parse(self, response):
        items:object = GpucrawlersItem()
        products:str = response.css(".productflex")
        for product in products:
            items['url'] = product.css('a::attr(href)').extract()
            yield items
