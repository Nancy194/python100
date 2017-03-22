# 题目：输出指定格式的日期。
import time
import datetime
f=1

if int(f)==1:
    print(time.strftime('%Y/%m/%d %H:%M:%S ',time.localtime(time.time())))

if int(f)==2:
    print(time.strftime('%d/%m/%Y %H:%M:%S ',time.localtime(time.time())))

#------------------------------------------------
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%Y'))

# 创建日期对象
q = datetime.date(1941, 1, 5)

print(q.strftime('%d/%m/%Y'))

# 日期算术运算
r = q + datetime.timedelta(days=1)

print(r.strftime('%d/%m/%Y'))

# 日期替换
s = q.replace(year=q.year + 1)

print(s.strftime('%d/%m/%Y'))
