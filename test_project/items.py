# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    score = scrapy.Field()
    is_accepted = scrapy.Field()
    answer_id = scrapy.Field()
    owner_reputation = scrapy.Field()
    owner_id = scrapy.Field()
    content = scrapy.Field()
    question_id = scrapy.Field()
