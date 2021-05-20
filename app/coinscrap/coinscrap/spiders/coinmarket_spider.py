import scrapy
from ..items import CoinscrapItem
class CoinmarketSpider(scrapy.Spider):
    name = 'coinmarket'
    start_urls = ['https://cryptonaute.fr/crypto-monnaie/'  
        ]
    def parse(self, response):

        items = CoinscrapItem()

        all_crypto = response.css('tr')
        for crypto in all_crypto:
            nom = crypto.css('a::text').extract()
            if nom == []:
                nom = crypto.css('b::text').extract()
            prix = crypto.css('td:nth-child(4)::text').extract()
            change = crypto.css('td.up::text').extract()
            if change == []:
                change = crypto.css('td.down::text').extract()
            marketcap = crypto.css('td:nth-child(6)::text').extract()
            vol24h = crypto.css('td:nth-child(7)::text').extract()
            offredispo = crypto.css('td:nth-child(8)::text').extract()
            numero = 1

            
            items['nom'] = nom
            items['prix'] = prix
            items['change'] = change
            items['marketcap'] = marketcap
            items['vol24h'] = vol24h
            items['offredispo'] = offredispo
            items['numero'] = numero



            yield items

