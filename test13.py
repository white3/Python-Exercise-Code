# coding=utf-8
# 旋转数组
def rotateArray(arr=[],n=0):
    swap(arr,n,len(arr)-1)
    swap(arr,0,n-1)
    swap(arr)
    return arr
# 数组倒序
def swap(arr=[],low=0,high=None):
    if high==None:  high=len(arr)-1
    while low<high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1;high-=1

print rotateArray([1,2,3,4,5,6,7,8,9],6)
