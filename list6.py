#coding=utf-8
def F(n):
    l=[0,1]
    a=0
    b=1
    for i in range(n-2):
        l.append(a+b)
        t=a
        a=b
        b=t+b
    print l
        
F(20)

def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b 
    return a

print fib(19)






'''
Created on 2016年8月15日

@author: Administrator
'''
