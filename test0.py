# coding=utf-8
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
实现：
'''
# for循环
print ["%d%d%d" % (i,j,k) for i in range(1,5) for j in range(1,5) if(i is not j) for k in range(1,5) if(k!=i and j!=k)]

# 递归实现 - 2017.10.08