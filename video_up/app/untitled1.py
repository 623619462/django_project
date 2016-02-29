# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:07:34 2016

@author: wangyu
"""

from pymongo import MongoClient
client = MongoClient('localhost',10001)
db=client.video_up
col=db.videos
video_name="test01"
video_url="url01"
result="normal"
post={"name":video_name,
"url":video_url,
"results":result}
#col.save(post)
for k in col.find():
    print k
client.close()
