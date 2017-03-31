__author__ = "Steven Lee"


a=0
b = a and 1 or 2

c = 0 and 1
print("0 and 1:", c)  # print 0 , 0和任意数做and 运算都是0

d = 0 or 2
print("0 or 2:", d)  # print 2