# 题目：输出一个随机数。

import random
import string
print(random.uniform(10,20)) # 生成一个指定范围内的随机符点数

print(random.random())  # 返回随机生成的一个实数，它在[0,1)范围内。

print(random.randint(10,20))  # 用于生成一个指定范围内的整数

print(random.randrange(10,20,3))
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。
# 如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。

list=[2,5,7,12,19,41,60]
print(random.choice(list))

random.shuffle(list)  # 用于将一个列表中的元素打乱。
print(list)

print(random.sample(list,3)) # 从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
