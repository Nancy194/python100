# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def fb(n,m):
    list=[m,m+1]
    for i in range(n):
        list.append(list[-1]+list[-2])
    return list

a=fb(18,1)
b=fb(18,2)
c=zip(a,b)
list=[]
for i,j in c:
    list.append(j/i)
    print(i,j)
print(sum(list))
# -------------------------
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    t = a
    a = a + b
    b = t
print(s)
