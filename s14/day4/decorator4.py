import time
__author__ = "Steven Lee"
# 函数就是一种“变量”
# a.把一个函数名当做实参传给另外一个函数(在不修改被装饰函数源代码的情况下为其添加功能)
# b.返回值中包含函数名(不修改函数的调用方式)


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)  # func(): run test1() ,test1 不会出错，但是test2会出错，因为没有传参数
        stop_time = time.time()
        print("the func run time is %s" % (start_time-stop_time))
    return deco


@timer  # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timer  # test2 = timer(test2) = deco  test2(name) = deco(name)
def test2(name, age):
    print("test2:", name, age)

# test1 = timer(test1)
# test1()  # ---> deco  没有改变test1的源代码

test1()
test2("stevenlee", "22")