# coding=utf-8
# 8.选择排序
def select_sort(numList=[]):
    if numList:
        lens = len(numList)
        for j in range(0,lens-1):
            flag = True
            for i in range(j+1,lens):
                if numList[j]>numList[i]:
                    temp = numList[j]
                    numList[j] = numList[i]
                    numList[i] = temp
                    flag = False
            if flag: break
    return numList
# 9.冒泡排序
def bubbling_sort(numList):
    for i in xrange(0,len(numList)):
        flag = True
        for j in xrange(0,len(numList)-i-1):
            if numList[j]>numList[j+1]:
                temp = numList[j]
                numList[j] = numList[j+1]
                numList[j+1] = temp
                flag = False
        if flag:break
    return numList
# 10.快速排序
def fast_sort(numList=[]):
    fast_sort_impl(low=0, high=len(numList)-1, numList=numList)
    return numList
def fast_sort_impl(low, high, numList):
    left,right,k=low,high,numList[high]
    if left>=right:return 0
    while left<right:
        while left<right and numList[left]<=k:  left+=1
        numList[right] = numList[left]
        while left<right and numList[right]>=k: right-=1
        numList[left] = numList[right]
    numList[right] = k
    fast_sort_impl(low,right-1,numList)
    fast_sort_impl(right+1,high,numList)
# 11.插入排序
def insert_sort(numList):
    for i in xrange(1,len(numList)):
        flag = True
        for j in xrange(0,i):
            if numList[j]>numList[i]:
                temp = numList[j]
                numList[j] = numList[j+1]
                numList[j+1] = temp
                flag = False
        if flag:break
    return numList
print select_sort([4,3,5,6,2,6,8])
print fast_sort([4,3,5,6,2,6,8])
print bubbling_sort([4,3,5,6,2,6,8])
print insert_sort([4,3,5,6,2,6,8])