import requests
from config import HOST
#【案例2】：教管系统-列出课程
#1.构造请求消息体
payload={'action':'list_course','pagenum':'1','pagesize':'20'}
#2.发送get请求
r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload)
# print(r.text.encode.decode('unicode_escape'))
print(r.content.decode('unicode_escape'))

print(r.text)
r.encoding='unicode_escape'
print(r.text)
print(r.json())
