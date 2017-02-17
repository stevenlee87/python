__author__ = "Steven Lee"
# a.把一个函数名当做实参传给另外一个函数(在不修改被装饰函数源代码的情况下为其添加功能)
# b.返回值中包含函数名(不修改函数的调用方式)


def add(a, b, f):
    return f(a) + f(b)

res = add(2, -3, abs)
print(res)
