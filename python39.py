# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

list=[1, 3, 5, 5, 7, 24, 26, 26, 43, 45, 47, 65, 75, 75, 345]

a=int(input('input a number:'))
list.append(a)

for i in range(len(list)-2):
    if (list[-1]>=list[i]) and (list[-1]<list[i+1]):
        t=i
print(t)
list1=list[0:t+1]
list2=list[t+1:-1]
print(list1,list2)

l=list1+list[-1:]+list2
print(l)

