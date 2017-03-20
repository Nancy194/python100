#题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

import math
for i in range(2000):
    x=i+100
    y=i+268
    if (x==int(math.sqrt(x))*int(math.sqrt(x))) and (y==int(math.sqrt(y))*int(math.sqrt(y))):
        print('x的平方根是 is ', math.sqrt(x))
        print('y的平方根',math.sqrt(y))
        print('this number are:',i)
