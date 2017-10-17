# coding=utf-8
'''
正整数分解质因数
题目：将一个正整数分解质因数。例如：输入 90,打印出 90=2*3*3*5。
程序分析：对 n 进行分解质因数，应先找到一个最小的质数 k，然后按下述步骤完成：
 (1)如果这个质数恰等于 n，则说明分解质因数的过程已经结束，打印出即可。
 (2)如果 n<>k，但 n 能被 k 整除，则应打印出 k 的值，并用 n 除以 k 的商,作为新的正整数你 n,重复执行第一步。
 (3)如果 n 不能被 k 整除，则用 k+1 作为 k 的值,重复执行第一步。
'''
import math
# 获取最小质数
def find_min_prime(num):
    for n in xrange(2,int(math.sqrt(num)+1)):
        if num%n==0:
            return n
    return num
# 获取分解质因数列表
def get_factorization_intoprimes(num):
    if num<1:   return False
    arr = []
    while True:
        temp = find_min_prime(num)
        arr.append(temp)
        if temp==num: break
        num /= temp
    return arr
#------------------------TEST-----------------------
n = 1024**5
out = str(n)+" = "
num_list = get_factorization_intoprimes(n)
for i in xrange(0,len(num_list)-1):out += str(num_list[i])+" * "
out += str(num_list[len(num_list)-1])
print out
#-----------------------输出优化----------------------
print n , "=", " * ".join(map(lambda x:str(x),get_factorization_intoprimes(n)))
#---------------------------------------------------
def getMaxRangePrimeNumList(maxNum):
    result=[]
    src=range(2,maxNum+1)
    while len(src)>0:
        #取出并移除集合第一个元素，该元素一定是质数
        a=src.pop(0)
        #移除集合里所有能够被该质数整除的数
        for i in src:
            if(i%a==0):src.remove(i)
        #将该质数添加到结果集中
        result.append(a)
    return result
def getPrimeFactorNumList(n):
    prime_num_list = getMaxRangePrimeNumList(n)
    result=[]
    while n != 1: # 循环保证递归
        for index in xrange(len(prime_num_list)) :
            prime_num = prime_num_list[index]
            if n % prime_num == 0:
                n /= prime_num # n 等于 n/index
                result.append(prime_num)
                break
    return result
def primeFactorization(n):
    print n, '=',
    if not isinstance(n, int) or n <= 0 :
        print '请输入一个正确的数字 !'
        exit(0)
    elif n == 1:
        print 1
    else:
        primeFactorNumList = getPrimeFactorNumList(n)
        print "*".join(map(lambda x:str(x),primeFactorNumList))
primeFactorization(90)
primeFactorization(100)
primeFactorization(54)