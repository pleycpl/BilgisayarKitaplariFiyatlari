# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ItbooksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DrItemLessInfo(Item):
    title       = Field()
    url         = Field()
    img         = Field()
    who         = Field()
    publisher   = Field()
    price       = Field()
    old_price   = Field()
    discount    = Field()
