# 题目：对10个数进行排序。
list1=[53,7,35,69,74,2,58,19,52,38]
list=[24,3,5,75,26,47,75,45,26,1,5,7,345,65,43]

n=len(list)
for i in range(n-1):
    for j in range(n-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print(list)

