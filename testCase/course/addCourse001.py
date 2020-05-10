from lib.courseLib import add,list
import time
courseName="大学英语"+str(int(time.time()*10000))

#1-1 先列出课程
retList0=list(1,400)
#1-2 再新增课程
ret=add(courseName,'课程描述','0')
print(ret)
if ret['retcode']==0:
    print(">>>>>新增课程测试通过1")
    #1-3 再次列出课程
    retList1=list(1,400)
    #怎么判断，我们新增的课程，在列表中？？
    # 1、（课程ID或者课程名称，在列表中存在）
    # 2、判断长度，如果新增课程之前的列表长度 + 1 = 新增课程之后的列表长度
    # print(retList0)
    # print(retList1)
    if len(retList0['retlist'])+1 ==len(retList1['retlist']):
        print(">>>>>新增课程测试通过2")
    if retList0['total'] + 1 == retList1['total']:
        print(">>>>>新增课程测试通过3")