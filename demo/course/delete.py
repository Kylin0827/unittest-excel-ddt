import requests
from config import HOST
#1.请求头
header={'Content-Type':'application/x-www-form-urlencoded'}
#2.构造请求消息体
payload={"action":"delete_course","id":2111}
#3.发送delete请求
r=requests.delete(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
print(r.text)
