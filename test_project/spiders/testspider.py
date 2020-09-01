""" """

import scrapy
import re

from test_project.items import TestProjectItem

from test_project.sqlutil import getQuestionIdById 
from test_project.sqlutil import setQuestionVisited 

class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['codereview.stackexchange.com']

    def start_requests(self):
        """生成url，请求并回调解析"""
        for i in range(1, 66639):
            question_id = getQuestionIdById(i)
            if question_id == 0:
                continue
            url = 'https://codereview.stackexchange.com/questions/{question_id}'.format(question_id = question_id)
            print("processing",question_id)
            yield scrapy.Request(url = url, callback = self.parse)
            setQuestionVisited(question_id)#设置该问题为已访问

    def parse(self, response):
        """解析html"""
        question_id = re.search('(?<=questions/)\d+', response.url).group()
        for line in response.xpath('//div[@id="answers"]/div[contains(@class,"answer")]'):
            item = TestProjectItem()
            item['score'] = line.xpath('.//div[@itemprop="upvoteCount"]/text()').extract()
            item['is_accepted'] = line.xpath('@itemprop').extract()
            item['answer_id'] = line.xpath('@data-answerid').extract()
            item['owner_reputation'] = line.xpath('.//div[contains(@class,"user-info")]/div[@class="user-details"]/div/span[@class="reputation-score"]/text()').extract()[-1]
            item['owner_id'] = line.xpath('.//div[contains(@class,"user-info")]/div[@class="user-details"]/a/@href').extract()[-1]
            item['content'] = line.xpath('.//div[@itemprop="text"]').extract()
            item['question_id']=question_id
            yield item
