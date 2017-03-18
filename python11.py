# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

# a=[1,1,2,3,5,8,...], b=[2,2,4,6,10,16...]

def feb(n):
    if n==1 or n==2:
        return 2
    list=[1,1]
    for i in range(2,n):
        list.append(list[-1]+list[-2])
    return list[-1]*2

print(feb(7))