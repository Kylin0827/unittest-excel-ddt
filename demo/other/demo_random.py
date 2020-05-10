import random
print(int(random.random()*10000000000000000))
print(random.randint(1000000,10000000000000))

import time
print(int(time.time()*1000000))   #从1970-01-01  00:00:00  到现在所经历过的毫秒数。

time1=str(int(time.time()*100))

str="大学英语{{courseName}}"
print(str.replace('{{name}}',time1))

abcd="你好,{{sss}}"
print(abcd.replace("{{sss}}","狗子"))
