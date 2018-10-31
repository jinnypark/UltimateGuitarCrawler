# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UgCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    meta_title = scrapy.Field() #2
    meta_description = scrapy.Field() #3
    #meta_image = scrapy.Field() #4
    #meta_artist = scrapy.Field() #
    #meta_contentDescription = scrapy.Field() #5
    meta_keywords = scrapy.Field() #6
    #meta_viewport = scrapy.Field() #8
    #meta_application_name = scrapy.Field() #12 
    #meta_csrf_token = scrapy.Field()#11
    URL = scrapy.Field() #take url that i am crawling 
    chords = scrapy.Field()

