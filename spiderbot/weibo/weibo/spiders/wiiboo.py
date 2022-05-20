import json

import scrapy

from ..items import WeiboItem

class WiibooSpider(scrapy.Spider):
    name = 'wiiboo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}'.format(i) for i in range(1,100)]

    def parse(self, response):
        photoWallDict = json.loads(response.text)

        data = photoWallDict['data'] if 'data' in photoWallDict else {}
        cards = data['cards'] if 'cards' in data else {}
        for card in cards:
            # 决定了数据录入的先后

            text = card['mblog']['raw_text'] if 'mblog' in card else None
            # 带有html标记
            # text = card['mblog']['text'] if 'mblog' in card else None
            # print(text)

            scheme = card['scheme'] if 'scheme' in card else None
            # print(scheme)



            item = WeiboItem()
            item['text'] = text
            item['scheme'] = scheme


            yield item
