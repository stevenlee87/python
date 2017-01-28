__author__ = "Steven Lee"


def test(*args):
    print(args)

test(1, 2, 3, 4, 5)
test(*[1, 2, 3, 4, 5])


def test1(x, *args):
    print(x)
    print(args)

test1(6, 7, 8, 9)


def test2(**kwargs):
    """
    **kwargs:把N个关键字参数，转换成字典的方式
    """
    print(kwargs)

test2(name='steven', age='20', sex='male')  # print {'name': 'steven', 'age': '20', 'sex': 'male'}
