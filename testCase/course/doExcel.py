from lib.excelManagerLib import readExcel,getNewExcel
from lib.sendCourseReqLib import sendCourseReq
import json
import time,pprint
path=r'E:\ProjectCodeForPy\APIAutoTest20200422\data\教管系统-测试用例V1.2.xls'
newPath=r'E:\ProjectCodeForPy\APIAutoTest20200422\report\教管系统-测试结果.xls'
#1-4 得到一个新工作簿
workBookNew=getNewExcel(path)
#1-5 从新工作簿中,得到工作表1,备用
workSheetNew=workBookNew.get_sheet(0)

#1-1 从Excel中读取工作表中的测试用例
retList=readExcel(path,0)
pprint.pprint(retList)
#1-2 循环发送请求
for i in range(0,len(retList)):
    time.sleep(0.0001)
    row =retList[i]
    # print(row)
    ret=sendCourseReq(row)
    # print(ret)
    colus7 = json.loads(row[6])  # 第7列的值
    # print(colus7)
    # 1-3 断言
    if ret['retcode']==colus7['code']:
        print(row[0]+'测试通过')
        #1-6 写工作表内容
        workSheetNew.write(i+1, 7 ,'测试通过') # 把结果写入第i+1 行,第8列
    else:
        print(row[0]+'测试不通过')
        workSheetNew.write(i + 1, 7, '测试不通过')# 把结果写入第i+1 行,第8列
        if  'reason' in ret.keys():# 测试不通过,不一定有原因,所以要判断返回值字典中是否存在reason 的key
            workSheetNew.write(i + 1, 8, ret['reason']) # 把原因写入第i+1 行,第9列
#1-7 保存工作簿
workBookNew.save(newPath)

