# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
a=input('请输入一串数字，用空格隔开：')
alist=a.strip().split(' ')
l=len(alist)
blist=[]
for i in alist:
    blist.append(int(i))

mi=min(blist)
ma=max(blist)

for i in range(l):
    if blist[i]==mi:
        x=i
    if blist[i]==ma:
        y=i

blist[-1],blist[x]=blist[x],blist[-1]
blist[0],blist[y]=blist[y],blist[0]
print(mi,ma)
print(blist)

