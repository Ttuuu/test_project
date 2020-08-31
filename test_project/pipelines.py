# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from test_project.sqlutil import addaAnswerRecord 
import re
import os
import math

class TestProjectPipeline:
    def save_content(self,item):
        filepath='./answer-content/{id}.txt'.format(id=item['answer_id'][0])
        path = filepath[0:filepath.rfind("/")]
        if not os.path.isdir(path):  # 无文件夹时创建
            os.makedirs(path)
        fd = open(filepath, mode="w", encoding="utf-8")
        fd.write(item['content'][0])
        fd.close()

    def process_item(self, item, spider):
        num=item['owner_reputation']
        if ',' in num:
            num=num.replace(',','')
        if 'k' in num:
            num=num.replace('k','')
            num=math.ceil(float(num)*100)
        item['owner_reputation']=num
        item['owner_id']=re.search('(?<=/users/)\d+', item['owner_id']).group()
        self.save_content(item)
        addaAnswerRecord(item)
        return item
