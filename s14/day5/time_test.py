import time
import datetime
__author__ = "Steven Lee"

# 1.timestamps transfer to strct_time
x = time.localtime(1491902421)
"""
print time.struct_time(tm_year=2017, tm_mon=4, tm_mday=11, tm_hour=17, tm_min=20, tm_sec=21, tm_wday=1, 
tm_yday=101, tm_isdst=0)
"""
print(x)

# print(help(x))

print(x.tm_year)  # print 2017

# 2.struct_time transfer to timestamps
print(time.mktime(x))  # print 1491902421.0 timestamps

# 3.struct_time transfer to format_string
print(time.strftime("%Y-%m-%d %H-%M-%S", x))  # print 2017-04-11 17-20-21

# 4.format_string transfer to struct_time
print(time.strptime("2017-04-11 17-20-21", "%Y-%m-%d %H-%M-%S"))
"""
print ime.struct_time(tm_year=2017, tm_mon=4, tm_mday=11, tm_hour=17, tm_min=20, tm_sec=21, tm_wday=1, 
tm_yday=101, tm_isdst=-1)
"""

# 5.struct_time transfer to %a %b %d %H:%M:%S %Y 串
print(time.asctime(x))  # print Tue Apr 11 17:20:21 2017

# 6.timestamps transfer to %a %b %d %H:%M:%S %Y 串
print(time.ctime(1491902421))  # print Tue Apr 11 17:20:21 2017

print("-----------------")
print(datetime.datetime.now())  # 2017-04-21 15:30:13.692924
print(time.time())
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2017-04-21

print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分
