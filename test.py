import time
import os
import ConfigParser
import math
import hashlib
import httplib
import json
import struct
import base64
import random
import uuid
import redis

r = redis.StrictRedis('192.168.130.236',6379,0)
list = [1,2,3,4,5]

r.lpush("list", *list)

# print r.get("name")
# flag = 1
# while flag == 1:
#     val = r.lpop('queue')
#     if val == None:
#         flag = 0
#     else:
#         print val



# print int(time.time())

# appkey = 'f3bb208b3d081dc8'
# SECRETKEY_MINILOADER = '1c15888dc316e05a15fdd0a02ed6584f'
# cid = '16402360'
# print hashlib.md5('cid={cid}&from=miniplay&player=1{SECRETKEY_MINILOADER}'.format(cid = cid, SECRETKEY_MINILOADER = SECRETKEY_MINILOADER)).hexdigest()

# def rc4(key, data):
# #all encryption algo should work on bytes
#     assert type(key)==type(data) and type(key) == type(b'')
    
#     state = list(range(256))
#     j = 0
#     for i in range(256):
#         j += state[i] + key[i % len(key)]
#         j &= 0xff
#         state[i], state[j] = state[j], state[i]

#     i = 0
#     j = 0
#     out_list = []
#     for char in data:
#         i += 1
#         i &= 0xff
#         j += state[i]
#         j &= 0xff
#         state[i], state[j] = state[j], state[i]
#         prn = state[(state[i] + state[j]) & 0xff]
#         out_list.append(char ^ prn)

#     return bytes(out_list)

# url = "http://aplay-vod.cn-beijing.aliyuncs.com/acfun/web?vid=58ad9f810cf2edf0addab8bb&ct=85&ev=2&sign=1_1495708394_b2520f7cacb652dad3d9d770b977ba51"

# conn = httplib.HTTPConnection("aplay-vod.cn-beijing.aliyuncs.com")
# conn.request(method="GET",url=url) 
# response = conn.getresponse()
# res= response.read()
# json_data = json.loads(res)
# enc_text = base64.b64decode(json_data['data'])
# dec_text = rc4(b'2da3ca9e', enc_text).decode('utf8')
# youku_json = json.loads(dec_text)