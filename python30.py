# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def huiwen(n):
    m=int(n)
    a = int(m / 10000)
    b = int(m % 10000 / 1000)
    c = int(m % 1000 / 100)
    d = int(m % 100 / 10)
    e = int(m % 10)

    if (a==e) and (b==d):
        return True
    else:
        return False

print(huiwen(14341))
