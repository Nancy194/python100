# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

import functools
def summ(a,m):
    n=m
    s=0
    list=[]
    sumlist=[]
    while m>0:
        list.append(a*pow(10,m-1))
        m=m-1
    for i in list:
        s+=i
    print(s)
    sumlist.append(s)
    for i in range(1,n):
        j=pow(10,i)
        sumlist.append(int(s/j))
    print(sumlist)
    q=0
    for i in sumlist:
        q+=i
    print(q)

summ(2,7)
#------------------------------
Tn = 0
Sn = []
n = int(input('n = :\n'))
a = int(input('a = :\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = functools.reduce(lambda x,y : x + y,Sn)
print(Sn)
