# 题目：求100之内的素数。

import math
list=[2]

for i in range(3,101):
    t=1
    k=int(math.sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            t=0
    if t==1:
        list.append(i)

print(list)


