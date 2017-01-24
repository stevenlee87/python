__author__ = "Steven Lee"


def test(x, y):  # x与y是形参
    print(x)
    print(y)

# test(1, 2)  # 1 和 2 是实参，实际占空间的参数。与形参一一对应
# test(y=2, x=1)  # 与形参顺序无关
test(3, y=2)  # (y=2)位置参数在关键字参数(3)后
# test(3, y=2, 6)  # positional argument follows keyword argument
