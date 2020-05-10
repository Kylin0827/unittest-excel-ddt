# 实现发送课程管理请求的函数，传入的是excel中的一行数据
from lib.courseLib import add,delete,list
import json
import time

def sendCourseReq(row):
    # print(row)  # 传入的是一行数据，也就是一个测试用例
    colus5=row[4]  #第5列的值
    # 第6列的值，用json.loads方法，把字符串转化为字典格式
    colus6 = json.loads(row[5])
    ret=None
    if colus5  =='add':
        # print(colus6['name'])# 课程名称
        courseName = colus6['name']  # 获取课程名称
        # 把关键字：{{courseName}} 替换成时间戳
        courseName = courseName.replace('{{courseName}}', str(int(time.time() * 100)))
        ret=add(courseName,colus6['desc'],colus6['display_idx'])
    elif colus5 =='list':
        ret=list(colus6['pagenum'],colus6['pagesize'])
    elif colus5 =='delete':
        ret = delete(colus6['id'])
    return ret


# path='E:\ProjectCodeForPy\APIAutoTest20200422\data\教管系统-测试用例V1.2.xls'
# # excelCases=redExcel(path,0)
# # sendCourseReq(excelCases[0])

# print(excelCases)