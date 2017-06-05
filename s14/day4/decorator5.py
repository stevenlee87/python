__author__ = "Steven Lee"
# 多个装饰器的调用顺序是自下往上，但是运行时的执行顺序是自上往下！！！

def deco_1(func):
    print("enter into deco_1")

    def wrapper(a, b):  # deco_2(addfunc) = deco_1(deco_2(addfunc))
        print("enter into deco_1_wrapper")
        func(a, b)
        print("over deco_1")
    return wrapper


def deco_2(func):
    print("enter into deco_2")

    def wrapper(a, b):  # addfunc=deco_2(addfunc)=wrapper addfunc(a, b) = wrapper(a, b)
        print("enter into deco_2_wrapper")
        func(a, b)
        print("over deco_2")
    return wrapper


@deco_1
@deco_2
def addfunc(a, b):
    print("result is ", a+b)

addfunc(3, 4)

# @deco_1
# @deco_2
# def addfunc(a, b):
#     print("result is ", a+b)
# 1.这个执行完成之后，会输出
# enter into deco_2
# enter into deco_1
# 此时addfunc已经被包装成了addfunc = deco_1(deco_2(addfunc))
# 2.执行addfunc(3, 4)
# 首先执行deco_1, 此时deco_1中的参数func为deco_2(addfunc)，进入wrapper，输出enter into deco_1_wrapper
# 然后执行wrapper中的func，即deco_2(addfunc)，进入deco_2中的wrapper，输出enter into deco_2_wrapper
# 此时的func 为addfunc本身，执行func(a, b)，输出了result is 7,接着输出了over deco_2,over deco_1