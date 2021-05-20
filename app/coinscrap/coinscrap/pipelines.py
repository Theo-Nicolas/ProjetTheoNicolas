# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from pymongo import MongoClient

class CoinscrapPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'mongodb_project',
            27017
        )
        db = self.conn['mycoin']
        self.collection = db['coin_tb']

    def process_item(self, item, spider):
            self.collection.find_one_and_update(
                {"nom": item["nom"]},
                {"$set": dict(item)},
                upsert=True
            )
            return item
