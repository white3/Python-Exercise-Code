# coding=utf-8
'''
筛素数
题目：指定最大范围 n，判断 2-n 之间有多少个素数，并输出所有素数(二分搜索筛选素数)
'''
import math

# ------ 二分搜索 ------
def binarySearch(numList ,destValue):
    low = 0
    high = len(numList)-1
    while low<=high:
        mid = (low + high) / 2
        if numList[mid] == destValue: return mid
        elif numList[mid] < destValue: low = mid + 1
        else: high = mid - 1
    return -mid-1
# ------ 筛选素数 ------
def getMaxRangePrimeNumList(maxNum):
    result = []
    src = range(2, maxNum+1)
    while len(src)>0:
        a = src.pop(0)
        for i in src:
            if i%a==0:src.remove(i)
        result.append(a)
    return result
def getRangePrimeNumList(minNum, maxNum):
    result=getMaxRangePrimeNumList(maxNum)
    index = abs(binarySearch(result, minNum))
    return result[index:]

result = getRangePrimeNumList(100, 200)
print "共有%d 个素数，素数列表为：" % len(result),result