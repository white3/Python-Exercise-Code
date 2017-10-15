# coding=utf-8
# 打印出所有的水仙花数
# 1
num = []
for n in range(100,1000):
    i = n/100
    j = n%100/10
    k = n%10
    if i**3 + j**3 + k**3 == n: num.append(n)
print num

# 2
print ["%d%d%d" % (i, j, k) for i in range(1,10) for j in range(10) for k in range(10) if(i**3 + j**3 + k**3 == i*100+j*10+k)]