'''
军事小队通过了王者峡谷后进入了埋宝之地，该地区被划分成了77777个从1开始具有唯一编号的小型区域。
根据历史传说，区域编号的数字中含有3或6的有野怪，其余区域有宝藏。
如区域56有野怪，而区域57有宝藏。请问军事小队一共可以获取到多少份宝藏。
'''
def getKing(num):
    numList = []
    result = 0
    for i in xrange(1,num+1):
        flag = True
        numList = map(lambda x:x,str(i))
        for j in numList:
            if j=='3' or j=='6':flag = False;break;
        if flag:result+=1;
    return result
print getKing(77777)