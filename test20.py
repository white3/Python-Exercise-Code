#coding=utf-8
'''
写一个方法，要求能获取 2 个字符串的所有的最大相同子串，返回一个集合
例如：getMaxPublicSubString("daccedbccfuhcfedjjfjba","dabccfedfjba")
运行结果为：[bccf, cfed, fjba]
'''
'''
思路：选出长度最大和最小的字符串
最小的字符串，从完整字符串开始，循环长度1 -1 截取指定长度的字符串
遍历这些截取出来的字符串，判断最大字符串中是否包含这个字符串，
若包含，则这个字符串是最大公共字符串
'''
def getMaxPublicSubString(str1,str2):
#三元表达式语法：为真时的结果 if 判定条件 else 为假时的结果
    maxstr=str1 if len(str1)>len(str2) else str2
    minstr=str2 if maxstr==str1 else str1
    result=[]
    flag=False
    #i 表示要截断的长度,范围从 0 到 len(minstr)-1
    for i in range(len(minstr)):
    #例如：字符串"abcd"被截断 2 个长度后，变成"ab","bc","cd",共需循环 3 次
    #实际起始截断范围是[0:len(minstr)-i]，结束截断范围[i:len(minstr)],则定义一个范围在 0~i 范围的变量 j 即可
        for j in range(i+1):
            substr=minstr[j:len(minstr)-i+j]
            #不等于-1 表示该子字符串存在于 maxstr 中
            if(maxstr.find(substr)!=-1):
                flag=True
                result.append(substr)
        if flag:
            return result
print getMaxPublicSubString( "dabccfedfjba", "daccedbccfuhcfedjjfjba")