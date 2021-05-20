# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinscrapItem(scrapy.Item):
    # define the fields for your item here like:
     nom = scrapy.Field()
     prix = scrapy.Field()
     change = scrapy.Field()
     marketcap = scrapy.Field()
     vol24h = scrapy.Field()
     offredispo = scrapy.Field()
     numero = scrapy.Field()

    
