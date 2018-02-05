# coding=utf-8
import json
import math
import requests
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

c_cookies = 'BDUSS=XXX'
headers = {
    'Host': 'pet-chain.baidu.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Origin': 'https://pet-chain.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'https://pet-chain.baidu.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': c_cookies}


def recall(pet_id):
    url = 'https://pet-chain.baidu.com/data/market/unsalePet'
    timestramp = int(round(time.time() * 1000))
    payload = {"petId": pet_id, "requestId": timestramp, "appId": 1, "tpl": ""}
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    # return json.loads(res.content)['errorMsg']
    emsg = json.loads(res.content)['errorMsg']
    print '撤回: ' + emsg
    return emsg


def sell(pet_id, amount):
    url = 'https://pet-chain.baidu.com/data/market/salePet'
    timestramp = int(round(time.time() * 1000))
    payload = {"petId": pet_id, "amount": amount, "requestId": timestramp, "appId": 1, "tpl": ""}
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    emsg = json.loads(res.content)['errorMsg']
    print '以' + str(amount) + '售出: ' + emsg


petId = "XXX"

while True:
    sell(petId, 1499)
    time.sleep(0.3)
    recall(petId)
    sell(petId, 19999)
    time.sleep(10)
    msg = recall(petId)

    if "有人购买" in msg:
        break

    time.sleep(2)
