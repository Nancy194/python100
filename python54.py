# 题目：取一个整数a从右端开始的4〜7位



def fs(n):
    t = 120
    m=(n&t)>>3
    print(m)

# fs(252)

print(~(~0<<4) )