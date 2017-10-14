#coding=utf-8
#打印 9*9 乘法口诀表
str = ""
for i in range(1,10):
    for j in range(1,i+1):
        str +=  "%dx%d = %d " % (j, i, i*j)
    str += "\n"
print str