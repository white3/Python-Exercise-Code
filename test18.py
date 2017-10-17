# coding=utf-8
dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# 十进制到任意进制的相互转换
def radix_change(num, radix):
    numArr = []
    result = num
    while result!=0:
         result, remainder = divmod(result, radix)
         numArr.append(dic[remainder])
    numArr.reverse()
    return ''.join(numArr)
# 任意进制到十进制的相互转换
def radix_to_ten(num, radix):
    num,n = str(num),0
    for ch in num.upper():
        n*=radix
        if ord(ch)>=ord('A'):
            n += ord(ch)-ord('A')+10
        else:
            n += int(ch)
    return n

print radix_change(20, 16)
print radix_change(20, 8)
print radix_change(20, 2)
print radix_to_ten(14, 16)
print radix_to_ten(24, 8)
print radix_to_ten(10100, 2)