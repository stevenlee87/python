import time
__author__ = "Steven Lee"

x = time.localtime(1491902421)
print(x)
# print(help(x))
print(x.tm_year)
print(time.mktime(x))

print(time.strftime("%Y-%m-%d %H-%M-%S", x))
