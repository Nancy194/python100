# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。


while True:
    a=int(input('please input a number:'))
    b=pow(a,2)
    print(b)
    if b<50:
        break
