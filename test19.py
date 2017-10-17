# coding=utf-8
# 题目 约瑟夫环 ：有 n 个人围成一圈，顺序排号。
# 从第一个人开始报数（从 1 到 3 报数），凡报到 3 的人退出圈子，
# 问最后留下的是原来第几号的那位。
def josepCircle(n):
    circle = range(1,n+1)
    n, index,result = 1, 0, []
    while len(circle)!=0:
        index += 1
        if (index >= len(circle)): index = 0
        n += 1
        if n%3==0:result.append(circle.pop(index));index-=1
    return result
print josepCircle(34)