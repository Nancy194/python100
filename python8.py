#题目：输出 9*9 乘法口诀表。
#1*1=1
#1*2=2 2*2=4
#1*3=3 2*3=6 3*3=9
#1*4=4 2*4...

for i in range(1,10):
    print()
    for j in range(1,i+1):
        t=i*j
        print('%d*%d=%d' % (j,i,t),end=' ')
