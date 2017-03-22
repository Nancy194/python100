# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
# 问最后留下的是原来第几号的那位。
'''
n=2  t=2
n=3  t=2
n=4  t=1
n=5  t=4
n=6   t=1
n=7   t=4
n=8   t=7
'''
def remove(list,x):
    if x in list:
        i=list.index(x)
        l=list[:i]+list[i+1:]
        return l
    else:
        return -1

def num(n):
    l1=[i for i in range(1,n+1)]
    for i in range(1,n+1):
        if i%3==0:
            l1=remove(l1,i)
    print(l1)

# list=[1,2,3,4,5,6]
# print(remove(list,3))
num(6)


