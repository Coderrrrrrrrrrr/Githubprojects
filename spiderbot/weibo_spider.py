import json

import requests
from pprint import pprint
import time

urls = ['https://m.weibo.cn/api/container/getIndex?containerid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}'.format(i) for i in range(1,100)]

headers = {
    'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'cookie':'WEIBOCN_FROM=1110003030; SUB=_2A25PgjmqDeRhGeBI71IX9i_FwjuIHXVsjUfirDV6PUJbkdAKLW_8kW1NRp7xVHrdsMGR9eu5QTRPtQDfogQyfcpu; _T_WM=64152793347; MLOGIN=1; XSRF-TOKEN=2d6b45; M_WEIBOCN_PARAMS=luicode=10000011&lfid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&fid=2304136640661997_-_WEIBO_SECOND_PROFILE_WEIBO&uicode=10000011'
}


for url in urls:
    print(url)
    time.sleep(1.1)
    resp = requests.get(url,headers=headers)
    # resp.text是str类型
    pprint(resp.text)

    # str转dict。Python中合法的字典都是单引号'
    photoWallDict = json.loads(resp.text)

    data = photoWallDict['data'] if 'data' in photoWallDict else {}
    cards = data['cards'] if 'cards' in data else {}
    for card in cards:
        scheme = card['scheme'] if 'scheme' in card else None
        print(scheme)

        text = card['mblog']['text'] if 'mblog' in card else None
        print(text)