# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
import xlwt
from itemadapter import ItemAdapter
import json

from scrapy.exporters import CsvItemExporter

from openpyxl import Workbook

# 保存为csv文件
class FtimesPipeline(object):
    def open_spider(self, spider):
        self.file = open('test.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, delimiter='~')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

#     保存为xlsx文件
class MapdataPipeline(object):
    wb = Workbook()
    ws = wb.active
    # 设置表头
    ws.append(['text', 'scheme'])

    def process_item(self, item, spider):
        # 添加数据
        line = [item['text'], item['scheme']]
        self.ws.append(line) # 按行添加
        self.wb.save('text.xlsx')
        return item

class RequestsPipeline:
    def process_item(self, item, spider):
        scheme = item['scheme']
        text = item['text']

        resp = requests.get(scheme)
        with open('./test.txt', 'wb') as f:
            f.write(resp.content)

        # resp = requests.get(src)
        # with open('./test.txt', 'w') as f:
        # with open('imgs/{}'.format(name),'wb') as f:
        #     f.write(resp.content)

        return item

class WeiboPipeline:
    def process_item(self, item, spider):
        return item
