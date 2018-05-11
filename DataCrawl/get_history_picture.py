# -*- coding: utf-8 -*-
"""
   Author :       kouyafei
   date：          2018/5/11
"""
import requests
import os

path = 'picture'
if not os.path.exists(path):
    os.makedirs(path)

rootUrl = 'https://api-staging.jfbapp.cn/quiz/'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'}
i = 0


for index in range(5,107):
    url = rootUrl + str(index)
    session = requests.Session()
    session.trust_env = False
    try:
        res = session.get(url,headers = headers).json()
        questions = res['questions']
        for item in questions:
            id = item['id']
            imageUrl = item['image']
            avgScore = item['avgScore']
            normalizedAvgScore = item['normalizedAvgScore']
            scorePath = path + '/' + str(normalizedAvgScore)
            if not os.path.exists(scorePath):
                os.mkdir(scorePath)
            picturePath = scorePath + '/' + str(id) + '_' + str(avgScore) + '_' + imageUrl[41:]
            with open(picturePath,'wb') as picture:
                i += 1
                pic = session.get(imageUrl,headers=headers).content
                picture.write(pic)
                print("已存储" + str(i) + "张图片")
    except:
        continue