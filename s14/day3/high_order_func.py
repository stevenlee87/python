__author__ = "Steven Lee"


def add(a, b, f):
    return f(a) + f(b)

res = add(2, -3, abs)
print(res)