# coding=utf-8
'''
二分搜索
用 2 分法快速在有序列表中找到指定元素在列表中的角标，若没有找到则返回-插入点-1(<0)的值
例如：
在有序列表 list1 中[1, 3, 8, 12, 23, 31, 37, 42, 48, 58]中查找值为 8 的记录的。
在有序列表 list1 中[1, 3, 8, 12, 23, 31, 37, 42, 48, 58]中查找值为 9(不存在，以负数形式返回插入点的位置)的记录。
'''
def binarySearch(numList ,destValue):
    low = 0
    high = len(numList)-1
    while low<high:
        mid = (low + high) / 2
        if numList[mid] == destValue: return mid
        elif numList[mid] < destValue: low = mid + 1
        else: high = mid - 1
    return -1

print binarySearch([1, 3, 8, 12, 23, 31, 37, 42, 48, 58], 9)
print binarySearch([1, 3, 8, 12, 23, 31, 37, 42, 48, 58], 3)