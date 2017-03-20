# 题目：按逗号分隔列表

from collections import Iterable

a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(str(i))  # join只能连接迭代对象，所以需要将数字转换为字符
s=','.join(b)
print(s)

l=(str(n) for n in a)   # l是生成器；
s1=','.join(l)          # Python使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才产生结果，而不是立即产生结果。
print(s1)

print(isinstance(l,Iterable))  # 判断l是否迭代