from lib.courseLib import add,list
import time
courseName="大学英语"+str(int(time.time()*10000))

#1-1 再新增课程
ret=add(courseName,'课程描述','0')
print(ret)
if ret['retcode']==0:
    print(">>>>>新增课程测试通过1")
    #1-2 列出课程
    retList1=list(1,400)
    isExit=True
    for data in retList1['retlist']:
        # print(data)
        if ret['id']==data['id']:
            print('>>>>>>新增课程测试通过2')
            isExit=False
            break

    if isExit :
        print('>>>>>>>测试不通过，列表中不存在')