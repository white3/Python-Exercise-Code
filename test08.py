# coding=utf-8
import math
def swap(numList,a,b):
    numList[a],numList[b]=numList[b],numList[a]
# 8.选择排序
def select_sort(numList=[]):
    if numList:
        lens = len(numList)
        for j in range(0,lens-1):
            flag = True
            for i in range(j+1,lens):
                if numList[j]>numList[i]:
                    swap(numList,i,j)
                    flag = False
            if flag: break
    return numList
# 9.冒泡排序
def bubbling_sort(numList):
    for i in xrange(0,len(numList)):
        flag = True
        for j in xrange(0,len(numList)-i-1):
            if numList[j]>numList[j+1]:
                swap(numList,j,j+1)
                flag = False
        if flag:break
    return numList
# 10.插入排序
def insert_sort(numList,low=0,high=None,incer=1):
    if high==None:   high = len(numList)
    for i in xrange(low+incer,high,incer):
        temp = numList[i]
        k = i
        while k>=incer and temp<numList[k-incer]:
            numList[k] = numList[k-incer]
            k-=incer
        numList[k] = temp
    return numList
# 11.快速排序
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
# 12.希尔排序
def shell_sort(arr=[],low=0,high=None):
    #d = int(math.sqrt(len(numList)))
    if high==None:high=len(arr)-1
    incr=(high-low+1)>>1
    while incr>=1:
        i=low
        while i<incr:
            insert_sort(arr,0,high,incr)
            i+=1
        incr/=2
    return arr

# -----------------TEST---------------------
print "list: [4, 3, 5, 6, 2, 6, 8]"
print select_sort([4,3,5,6,2,6,8])
print fast_sort([4,3,5,6,2,6,8])
print bubbling_sort([4,3,5,6,2,6,8])
print insert_sort([4,3,5,6,2,6,8])
print shell_sort([4,3,5,6,2,6,8])