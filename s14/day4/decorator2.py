__author__ = "Steven Lee"
# 函数就是一种“变量”


def foo():
    print('in the foo')
    bar()


def bar():
    print('in the bar')

foo()
