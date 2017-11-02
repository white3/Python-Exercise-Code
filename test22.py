# coding=utf-8
# 字符串组合问题
# 编程列出一个字符串的全字符组合情况，原始字符串中没有重复字符
# 例如：
# 打印排列 permutation 情况： "abc" "acb" "bac" "bca" "cab" "cba"
# 23.字符串全排列问题
def swap(arr, i, j): arr[i],arr[j]=arr[j],arr[i]
def permutationStr(str):
    result = []
    def permutationDao(chars, begin):
        if begin==len(chars):result.append(''.join(chars))
        for i in xrange(begin, len(chars)):
            swap(chars ,i ,begin)
            permutationDao(chars, begin+1)
            swap(chars ,begin ,i)
    permutationDao([x for x in str], 0)
    result = map(lambda x: x,set(result))
    return ' '.join(result),len(result)
print permutationStr('alllll')
print "----------------------------------------------------------------------------------------"
# 打印组合 combination 情况： "a" "b" "c" "ab" "ac" "bc" "abc"
# 24.字符串全组合问题
def combinationStr(str):
    result = []
    temp = []
    def combinationStrDao(ch, pos, num):
        if num==0:result.append(''.join(temp));return;
        if pos==len(ch):return
        temp.append(ch[pos])
        combinationStrDao(ch, pos+1, num-1)
        temp.pop(len(temp)-1)
        combinationStrDao(ch, pos+1, num)
    strLen = [x for x in str]
    for i in xrange(1,len(strLen)+1):
        combinationStrDao(strLen, 0, i)
    return result
print combinationStr('abc')
print "----------------------------------------------------------------------------------------"
# 原始字符串是"abc"，打印得到下列所有排列组合情况
# "a" "b" "c"
# "ab" "bc" "ca" "ba" "cb" "ac"
# "abc" "acb" "bac" "bca" "cab" "cba"
# 25.字符串全排列组合问题
# 思路分析：
# 每行字符个数都是递增 ，下一行的字符是建立在上一行的基础上得到的
# 即在将第一行字符串长度限定为 1，第二行为 2....，
# 在第一行数据基础上{a,b,c}，创建第二行数据，
# 遍历字符串中所字符，并与第一行数据组合。注意每行字符串长度限制
# 1、先将原始字符串转换成字符数组 ch
# 2、将原始字符串每个字符添加到 Arraylist<String> list 集合中
# 3、遍历 list 集合用每个元素 str 去查找是否存在数组 ch 中的元素，如果 ch 中的字符 c 没有被 str 找到则用 str+c 作为新集合的值
# 返回;
# 4、遍历新集合重复 3 步骤
def permComStr(str):
    strMap = {}
    def getDeriveList(List):
        result = []
        for i in List:
            for j in str:
                if i.find(j)==-1:result.append(i+j);
        return result
    strList = [x for x in str]
    strMap[0] = strList
    for i in xrange(1,len(str)):
        strList = getDeriveList(strList)
        strMap[i] = strList
    return strMap
print permComStr('abcd')
print "----------------------------------------------------------------------------------------"
