# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。


week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

a=input('please input first letter:')
if a.lower()=='m':
    print('Monday')
elif a.lower()=='w':
    print('Wednesday')
elif a.lower()=='f':
    print(week[4])
elif a.lower()=='t':
    b=input('please input second letter:')
    if b.lower()=='u':
        print(week[1])
    elif b.lower()=='h':
        print(week[3])
    else:
        print('Error string!')
elif a.lower()=='s':
    c=input('please input second letter:')
    if c.lower()=='a':
        print(week[5])
    elif c.lower()=='u':
        print(week[6])
    else:
        print('Error string!')
