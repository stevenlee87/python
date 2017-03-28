__author__ = "Steven Lee"
# func = func_b() 执行后的结果就相当于 func = func_a，那么func('wang')其实就是func_a('wang')


def func_a(name):
    print('hi %s' % name)


def func_b():
    return func_a

func = func_b()

func('Alex')
