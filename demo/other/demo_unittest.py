import unittest
from lib.excelManagerLib import readExcel,getNewExcel
from lib.sendCourseReqLib import sendCourseReq
import json
import time
from lib.courseLib import add,list,delete
from ddt import ddt,data

path = r"D:\PycharmProjects\APIAutoTest20200422\data\教管系统-测试用例V1.2.xls"
# 1-1 从Excel中读取工作表中的测试用例
retList = readExcel(path, 0)

print(retList)
# 定义一个类，继承TestCase
@ddt
class  DemoUnittest(unittest.TestCase):
    # 1-1 类级别的环境初始化
    @classmethod
    def setUpClass(cls):
        cls.clearData()

    #1-2 类级别的环境清除
    @classmethod
    def tearDownClass(cls):
        cls.clearData()


    #1-3 环境清除方法
    @classmethod
    def clearData(cls):
        # 1.调用列出课程接口
        retList = list(1, 400)
        num = 0
        # 2.循环删除课程
        for data in retList['retlist']:
            delete(data['id'])
            num = num + 1
        print('本次共删除了:', num, '条数据')

    #1-4 Excel中的测试用例

    @data(*retList)
    def test001(self,row):
        print(row)
        time.sleep(0.0001)
        ret = sendCourseReq(row) # ret 是接口返回值
        colus7 = json.loads(row[6])  # 第7列的值
        # 1-3 断言
        v_reason=''
        if 'reason' in ret.keys():
            v_reason=ret['reason']
        self.assertEqual(ret['retcode'],colus7['code'],v_reason)
        print('测试成功!')


    #1-5 新增课程测试用例
    def test003(self):
        courseName = "大学英语" + str(int(time.time() * 10000))
        # 1-1 先列出课程
        retList0 = list(1, 400)
        # 1-2 再新增课程
        ret = add(courseName, '课程描述', '0')
        print(ret)
        #1-3 断言1
        self.assertEqual(ret['retcode'] ,0,'新增课程失败1')
        print(">>>>>新增课程测试通过1")
        # 1-4 再次列出课程
        retList1 = list(1, 400)
        #1-5 断言2
        self.assertEqual(retList0['total'] + 1,retList1['total'],'新增课程失败2')
        print(">>>>>新增课程测试通过3")



    @unittest.skip('skip的原因')
    def test002(self):
        print('方法二调用了')

