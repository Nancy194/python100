# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

list=[1,2,3,4,5,6,7,8,9,0]

def a(list,m):
    l=len(list)
    list1=list[:l-m]
    list2=list[l-m:]
    print(list2+list1)

a(list,11)