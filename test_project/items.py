# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    score = scrapy.Field()#评分
    is_accepted = scrapy.Field()#是否为被采纳回答
    answer_id = scrapy.Field()#回答id
    owner_reputation = scrapy.Field()#回答者reputation
    owner_id = scrapy.Field()#回答者id
    question_id = scrapy.Field()#问题id
