import requests
from config import HOST
#【案例5】：用户登录
header={'Content-Type':'application/x-www-form-urlencoded'}
#2.构造请求消息体：选口诀2
payload={'username':'auto','password':'sdfsdfsdf'}
#3.发送post请求
r=requests.post(f'{HOST}/api/mgr/loginReq',headers=header,data=payload)
#4.输出sessionid的值
print(r.cookies['sessionid'])
print(r.text)


