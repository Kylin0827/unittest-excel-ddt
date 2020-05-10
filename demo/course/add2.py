import requests
from config import HOST
import json
#【案例4】：教管系统-新增课程2
#1.请求头
h={'Content-Type':'application/json'}
#2.构造请求消息体：选口诀4：json 字典--->json字符串
payload1={
  'action' : 'add_course_json',
  'data':{"name":"初中化学","desc":"初中化学课程","display_idx":"1"}
}
payload2={
  'action' : 'add_course_json',
  'data':'''{"name":"初中化学","desc":"初中化学课程","display_idx":"1"}'''
}
#3.发送post请求
r=requests.post(f'{HOST}/apijson/mgr/sq_mgr/',headers=h,
                json=payload1 )
print((json.loads(r.text)))
print((json.dumps(r.json())))
print((r.json()))

