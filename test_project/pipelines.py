# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
"""scrapy框架的管道 清理数据并调用数据库操作"""

from itemadapter import ItemAdapter
import re
import os
import math

from test_project.sqlutil import addaAnswerRecord 


class TestProjectPipeline:

    def save_content(self,item):
        """保存评论文本内容为txt文档"""
        filepath = './answer-content/{id}.txt'.format(id = item['answer_id'][0])
        path = filepath[0 : filepath.rfind("/")]
        if not os.path.isdir(path):  # 无文件夹时创建
            os.makedirs(path)
        fd = open(filepath, mode = "w", encoding = "utf-8")
        fd.write(item['content'][0])
        fd.close()

    def process_item(self, item, spider):
        """数据格式化处理"""
        num = item['owner_reputation']  # 可能的值：13.2k 1,223 等（暂时还没有百万级数据）
        if ',' in num:
            num=num.replace(',','')
        if 'k' in num:
            num = num.replace('k','')
            num = math.ceil(float(num) * 100)
        item['owner_reputation'] = num
        item['owner_id'] = re.search('(?<=/users/)\d+', item['owner_id']).group()  #原有格式为/users/{id}/{username} 通过正则取到id
        self.save_content(item)
        addaAnswerRecord(item)
        return item
