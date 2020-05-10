import xlrd
from xlutils.copy import copy   #pip install xlutils
#一、设计一个读取excel 中数据的函数
# 功能：传递excel的路径+名称、第几个工作表,返回数据列表
def readExcel(path,sheet_num):
# 1-1 打开Excel，获取【workBook】 对象
    workBook=xlrd.open_workbook(path)

    #print(workBook.nsheets)#工作簿中有几个工作表
# 1-2 从工作簿中，获取【workSheet】对象
    workSheet = workBook.sheet_by_index(sheet_num)
    #print(workSheet.nrows)#工作表中有多少行数据
# 1-3 对【workSheet】工作表进行循环-逐行取出数据--放入列表中
    retList=[]
    for i in range(1,workSheet.nrows):#range左包含右不包含  读45条记录。【1-46）
        oneRow=workSheet.row_values(i)#返回的是一个list,得到的是第几行数据
        retList.append(oneRow)
        #print(type())oneRow
# 1-4 返回数据列表
    return retList

#二.设计工作簿复制函数
def getNewExcel(path):
    #1-1打开工作簿
    workBook=xlrd.open_workbook(path,formatting_info=True)
    # print(workBook.nsheets)

    # 1-2复制
    newWorkBook=copy(workBook)
    # 1-3 返回新的工作簿
    return newWorkBook

# path='E:\ProjectCodeForPy\APIAutoTest20200422\data\教管系统-测试用例V1.2.xls'
# newWorkBook=getNewExcel(path)
# savePath='E:\ProjectCodeForPy\APIAutoTest20200422\data\教管系统-测试用例V1.11111.xls'
# newWorkBook.save(savePath)


#
# path='E:\ProjectCodeForPy\APIAutoTest20200422\data\教管系统-测试用例V1.2.xls'
# excelCases=readExcel(path,0)
# print(excelCases)
#
# newWorkBook=getNewExcel(path)
# newPath=''
# newWorkBook.save(newPath)