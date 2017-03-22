# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
from math import sqrt
from sys import stdout

def prime(n):
    h = []
    leap = 1
    for m in range(2,n+1):
        k = int(sqrt(m + 1))
        for i in range(2,k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            h.append(m)
        leap=1
    return h

def despair(n):
    if n==0:
        return [0]
    m=n
    list=[]
    for i in prime(100):
        while n%i==0:
            list.append(i)
            n=n/i
    return list

def FinishNumber(n):
    for i in range(1,n):
        # print(despair(i),end='')
        # print(sum(despair(i)),end='  ')
        if sum(despair(i))+1==i:
            print(i)

FinishNumber(1000)

