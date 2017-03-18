#coding=utf-8
m=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and (j!=k)and(j!=k):
                print i,j,k 
                m.append(i*100+j*10+k)
print m
    
    
    

'''
Created on 2016年7月20日

@author: Administrator
'''
