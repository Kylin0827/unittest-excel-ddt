import requests
from config import HOST
import time
# 1.请求头
header={'Content-Type':'application/x-www-form-urlencoded','md5body':''}
#2.请求消息体
name="大学英语11"#+str(int(time.time()*100))

payload={'action':'add_course','data':f"""{{"name":"{name}",
  "desc":"初中化%26学课程",
  "display_idx":"4"}}"""}
print(payload)
#3.发送post请求{
r=requests.post(f'{HOST}/api/mgr/sq_mgr/',
                headers=header,
                data= payload)

print(r.json())
