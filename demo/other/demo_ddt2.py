import unittest
from ddt import ddt,data,unpack

excelData=[    ['1','2'],['4','5']     ]
# excelData=[(1,2),(3,4)]
# excelData=[{'aaa':'bbb'},{'aaa1':'bbb'}]


@ddt
class DemoDDT(unittest.TestCase):

    @data(*excelData)
    def test_001(self,data):
        print(data)
