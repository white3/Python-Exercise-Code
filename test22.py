# coding=utf-8
# 字符串组合问题
# 编程列出一个字符串的全字符组合情况，原始字符串中没有重复字符
# 例如：
# 打印排列 permutation 情况：
# "abc" "acb" "bac" "bca" "cab" "cba"
# 23.字符串全排列问题
def swap(arr, i, j): arr[i],arr[j]=arr[j],arr[i]
def permutationStr(str):
    result = []    
    def permutation(chars, begin):
        if begin==len(chars):result.append(''.join(chars))
        for ch in xrange(begin, len(chars)):
            swap(chars, begin, ch)
            permutation(chars, begin+1)
            swap(chars, begin, ch)
    permutation([x for x in str], 0)
    result = map(lambda x: x,set(result))
    return ' '.join(result),len(result)
print permutationStr('alllll')
def permutationStr2(str):
    result = []
    def permutation2(ch, pos=0):
        if pos==len(ch):result.append(''.join(ch))
        for n in xrange(pos,len(ch)):
            swap(ch,n,pos)
            permutation2(ch, pos+1)
            swap(ch,n,pos)
    
    permutation2([x for x in str])
    return result
print permutationStr2('abc')
# 打印组合 combination 情况：
# "a" "b" "c" "ab" "ac" "bc" "abc"
# 24.字符串全组合问题

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
