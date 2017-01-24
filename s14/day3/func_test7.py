__author__ = "Steven Lee"


def test(*args):
    print(args)

test(1, 2, 3, 4, 5)
test(*[1, 2, 3, 4, 5])


def test1(x, *args):
    print(x)
    print(args)

test1(6, 7, 8, 9)
