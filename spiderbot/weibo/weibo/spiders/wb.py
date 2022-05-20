import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pprint import pprint
import time
import requests

import re


class WbSpider(CrawlSpider):
    name = 'wb'
    allowed_domains = ['weibo.com']
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}'.format(i) for i in range(1,100)]

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie': 'WEIBOCN_FROM=1110003030; SUB=_2A25PgjmqDeRhGeBI71IX9i_FwjuIHXVsjUfirDV6PUJbkdAKLW_8kW1NRp7xVHrdsMGR9eu5QTRPtQDfogQyfcpu; _T_WM=67407663643; MLOGIN=1; XSRF-TOKEN=273c11; M_WEIBOCN_PARAMS=luicode=10000011&lfid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&fid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&uicode=10000011; mweibo_short_token=1389147429'
    }

    # def start_requests(self):
    #     cookies='WEIBOCN_FROM=1110003030; SUB=_2A25PgjmqDeRhGeBI71IX9i_FwjuIHXVsjUfirDV6PUJbkdAKLW_8kW1NRp7xVHrdsMGR9eu5QTRPtQDfogQyfcpu; _T_WM=67407663643; MLOGIN=1; XSRF-TOKEN=273c11; M_WEIBOCN_PARAMS=luicode=10000011&lfid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&fid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&uicode=10000011; mweibo_short_token=1389147429'
    #     cookies={i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
    #     for url in self.start_urls:
    #         print(url)
    #         time.sleep(1.1)
    #         resp = requests.get(url, headers=self.headers)
    #     yield scrapy.Request(
    #         self.start_urls[0],
    #         callback=self.parse,
    #         cookies=cookies
    #     )
    #     return resp

    def parse(self,response):
        print(response.text)
        pass
        # photoWallDict = json.loads(resp.text)
        #
        # data = photoWallDict['data'] if 'data' in photoWallDict else {}
        # cards = data['cards'] if 'cards' in data else {}
        # for card in cards:
        #     scheme = card['scheme'] if 'scheme' in card else None
        #     print(scheme)
        #
        #     text = card['mblog']['text'] if 'mblog' in card else None
        #     print(text)

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
