#coding=utf-8
from __future__ import division

m=[]
n=[]

for x in range(2,10000):
    for i in range(2,5000):
        if (x+100)/i==i:
            m.append(x)
        if (x+268)/i==i:
            n.append(x)
print m
print n 
print 

for i in m:
    if i in n:
        print i,










'''
Created on 2016年7月21日

@author: Administrator
'''
