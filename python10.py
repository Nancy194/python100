# 题目：暂停一秒输出，并格式化当前时间。
import time
a=[1,2]

for i in a:
    print(i)
    time.sleep(1)

print(time.time())
print('time() -- 返回当前时间戳，浮点数形式。不接受参数')

print(time.localtime(time.time()))
print('localtime() -- 将时间戳转换为本地时间元组格式。接受一个浮点型时间戳参数，其默认值为当前时间戳。')


print('strftime() -- 将时间元组以指定的格式转换为字符串形式。接受字符串格式化串、时间元组。时间元组为可选，默认为localtime()')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))