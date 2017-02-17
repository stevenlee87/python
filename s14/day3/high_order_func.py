__author__ = "Steven Lee"
# a.把一个函数名当做实参传给另外一个函数
# b.返回值中包含函数名


def add(a, b, f):
    return f(a) + f(b)

res = add(2, -3, abs)
print(res)
