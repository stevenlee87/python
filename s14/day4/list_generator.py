__author__ = "Steven Lee"

# 列表生成式
a = [i*2 for i in range(10)]
print(a)
print(a[2])

# 生成器
# 生成器不能用切片的方式去取，只能一个一个的去取
# 生成器只有在调用时才会生产相应的数据
# 生成器只记录当前的位置
# 生成器只有一个__next__()方法, next()
b = (i*2 for i in range(10))
b.__next__()
