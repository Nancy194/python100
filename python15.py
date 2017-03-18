# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def credit(n):
    if n>=90:
        print('A')
    elif 60<n<89:
        print('B')
    elif n<60:
        print('C')
    else:
        print('error credit')

credit(87)
credit(100)
credit(56)
credit(89.6)