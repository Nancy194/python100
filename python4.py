#题目：输入某年某月某日，判断这一天是这一年的第几天？

date=input('输入时间，格式为年月日，例：2016 02 18 \n')

d=date.split(' ')
year=int(d[0])
month=int(d[1])
day=int(d[2])

if (year%4==0) and ((year%100)!=0):
    leap=1
else:
    leap=0

months = (0,31,59,90,120,151,181,212,243,273,304,334)

t=months[month-1]+day
if (month>2) and (leap==1):
    t+=1
2
print('这是这一年的第 %dth 天' %t)
