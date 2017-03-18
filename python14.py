# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

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
    print('%d have below prime:'% m)
    print(list)
    for j in list:
        print(j)


print(prime(100))
despair(7)


print()
print('---------------------------------')
print('{} = '.format(2))
