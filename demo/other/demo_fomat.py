# '你好xxxxx先生'
# '你好{xxxxx}先生'
# '你好{{xxxxx}}先生'

name='tom'
#format 字符串格式函数,它的特点是【牺牲】一对大括号{}
print(f'你好{name}先生')  #1-无
print(f'你好{{{name}}}先生')#3-1
print(f'你好{{{{{name}}}}}先生')#5-2
print(f'你好{{{{{{{name}}}}}}}先生')#7-3















