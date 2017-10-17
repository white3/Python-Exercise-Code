#coding=utf-8
'''
简单电话传递数据加密
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上 5,
然后用和除以 10 的余数代替该数字，
再将第一位和第四位交换，第二位和第三位交换
'''
def encrypt(numStr):
    if len(numStr)!=4: return False
    encryptArray = map(lambda x: str((int(x) + 5) % 10), numStr)
    encryptArray[0],encryptArray[3] = encryptArray[3],encryptArray[0]
    encryptArray[1],encryptArray[2] = encryptArray[2],encryptArray[1]
    return "".join(encryptArray)
def deciphering(encryptStr):
    decipherArray = map(lambda x: int(x), encryptStr)
    decipherArray[0],decipherArray[3] = decipherArray[3],decipherArray[0]
    decipherArray[1],decipherArray[2] = decipherArray[2],decipherArray[1]
    decipherArray = map(lambda x: str((x+5)%10), decipherArray)
    return "".join(decipherArray)
a = raw_input('输入需要加密的数字：\n')
print "加密中-------------------------加密成功"
a = encrypt(a)
print a
print "解密中-------------------------解密成功"
print deciphering(a)
# print " * ".join(map(lambda x:str(int(x)**13),'1234'))