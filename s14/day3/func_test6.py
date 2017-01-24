__author__ = "Steven Lee"


# 默认参数


def test(x, y=2):
    print(x)
    print(y)


test(3, 6)
test(3)

# 默认参数特点：调用函数的时候，默认参数非必须传递
