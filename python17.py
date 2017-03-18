# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


def sta(s):
    letter=0
    space=0
    digit=0
    other=0
    for i in s:
        if i.isalpha():
            letter+=1
        elif i.isspace():
            space+=1
        elif i.isdigit():
            digit+=1
        else:
            other+=1
    print(letter,space,digit,other)

sta('dAFGGFwe12 e')

f='s'
print(f.isalpha())