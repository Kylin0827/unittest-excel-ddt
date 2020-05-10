import requests
from config import HOST
# 1.新增课程
def add(name,desc,display_idx):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'action': 'add_course', 'data': f"""{{"name":"{name}",
      "desc":"{desc}",
      "display_idx":"{display_idx}"}}"""}
    r = requests.post(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}

# 2.列出课程
def list(pagenum,pagesize):
    payload = {'action': 'list_course', 'pagenum':pagenum, 'pagesize': pagesize}
    r = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=payload)
    try:
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}

# 3.删除课程
def delete(id):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {"action": "delete_course", "id": id}
    r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}
#4.修改课程
def modify(id,name,desc,display_idx):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'action': 'modify_course', 'id': id, 'newdata': f'''{{
      "name":"{name}",
      "desc":"{desc}",
      "display_idx":"{display_idx}"
    }}'''
    }
    r = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}

#5.新增课程2
def add2(name,desc,display_idx):
    h = {'Content-Type': 'application/json'}
    payload = {
        'action': 'add_course_json',
        'data': {"name": name, "desc": desc, "display_idx": display_idx}
    }
    r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', headers=h,
                      json=payload)
    try:
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}

