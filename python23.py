#题目：打印出如下图案（菱形）:
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *
from sys import stdout

list=[1,3,5,7,5,3,1]

for i in list:
    for j in range(1,i+1):
        print('*',end='')
    print()

#-----------------------
for i in range(4):
    for j in range(2 - i + 1):
        print(' ',end='')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print()