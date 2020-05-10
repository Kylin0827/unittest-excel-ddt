import hashlib

#1-1 待加密的字符串
str='111111'
#1-2  实例化一个sha256对象
sha256=hashlib.sha256()
#1-3  调用update方法进行加密
sha256.update(str.encode('utf-8'))
#1-4 调用hexdigest方法,获取加密结果
print(sha256.hexdigest())
#结果为：bcb15f821479b4d5772bd0ca866c00ad5f926e3580720659cc80d39c9d09802a

