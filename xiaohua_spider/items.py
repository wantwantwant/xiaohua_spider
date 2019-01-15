# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    folder_name = scrapy.Field()
    img_name = scrapy.Field()       # 20190cLVqR.jpg
    img_url = scrapy.Field()        # https://www.aaa.com/api/20190cLVqR.jpg
    # img_bytes = scrapy.Field()    # b'\3e\01\
