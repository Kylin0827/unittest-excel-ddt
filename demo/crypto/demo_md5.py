import hashlib

#1-1 待加密的字符串
str='111111'
#1-2  实例化一个md5对象
md5=hashlib.md5()
#1-3  调用update方法进行加密
md5.update(str.encode('utf-8'))
#1-4 调用hexdigest方法,获取加密结果
print(md5.hexdigest())
