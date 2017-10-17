# coding=utf-8
'''
杨辉三角有多种重要的性质：
每行端点与结尾的数为 1.
每个数等于它上方两数之和。
每行数字左右对称，由 1 开始逐渐变大。
第 n 行的数字有 n 项
要求输入指定高度 n，例如 n=10 打印如下形式的杨辉三角形状：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
'''
def print_YH_Triangle(n):
    an = [1]*n
    for i in xrange(n):
        for j in xrange(i-1,0,-1):
            an[j]+=an[j-1]
        print "\t".join(map(lambda x:str(x),an[0:i+1]))
print_YH_Triangle(10)