import base64

#1-1 待加密的字符串
str='111111'

#1-2 base6编码
pwd=base64.b64encode(str.encode('UTF-8'))
print(pwd)

#1-3 base64解码
bstr=base64.b64decode(pwd)
print(bstr.decode('UTF-8'))