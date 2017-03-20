#题目：输入三个整数x,y,z，请把这三个数由小到大输出

m=input('输入三个整数，用空格键分开：\n')
list=m.split(' ')
list=sorted(list)
for i in list:
    print(int(i))