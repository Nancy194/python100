# 题目：求1+2!+3!+...+20!的和。

def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

sum=0
for i in range(1,21):
    print(factorial(i))
    sum=factorial(i)+sum

print(sum)