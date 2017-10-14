# coding=utf-8
# 计算指定范围的素数
# 题目：判断 101-200 之间有多少个素数，并输出所有素数
import math
def getPrimeNumber(left, right):
    list = []
    for i in range(left, right):
        flag = True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0: flag = False; break
        if flag : list.append(i)
    return list

print getPrimeNumber(100,200)