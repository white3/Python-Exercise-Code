# coding=utf-8
# 找出完数题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如 6=1＋2＋3.编程找出 1000 以内的所有完数
for num in range(1,1001):
    primeFactorList=[]
    sum=0
    for primeFactor in xrange(1,num):
        if num % primeFactor == 0:
            primeFactorList.append(primeFactor)
            sum+=primeFactor
    if(num==sum):
        print num,primeFactorList