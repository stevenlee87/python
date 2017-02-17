import time
__author__ = "Steven Lee"
# 函数就是一种“变量”
# a.把一个函数名当做实参传给另外一个函数
# b.返回值中包含函数名

# def foo():
#     print('in the foo')
#     bar()
#
#
# def bar():
#     print('in the bar')
#
# foo()


def timer(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func run time is %s' % (stop_time-start_time))  # stop_time减去start_time


def test1():
    time.sleep(3)
    print('in the test1')

timer(test1)  # 改变了函数的调用方式
# test1()
