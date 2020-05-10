import requests
from config import HOST
#1.请求头
header={'Content-Type':'application/x-www-form-urlencoded'}
#2.构造请求消息体
payload={'action':'modify_course','id':2112,'newdata':'''{
  "name":"初中化学abbbbb",
  "desc":"初中化学课程",
  "display_idx":"4"
}'''
}
#3.发送put请求
r=requests.put(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
print(r.text)
