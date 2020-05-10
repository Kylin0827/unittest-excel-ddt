import requests
from config import HOST
#用户登录函数
def login(username,password):
    #1.构造请求消息体
    header={'Content-Type':'application/x-www-form-urlencoded'}
    #2.构造请求消息体：口诀2
    payload={'username':username,'password':password}
    #3.发送Post请求
    r=requests.post(f'{HOST}/api/mgr/loginReq',headers=header,data=payload)
    try:
        # return r.json()
        return r.cookies['sessionid']
    except:
        # return {'retcode': 888, 'reason': '项目异常'}
        return '1111111'

