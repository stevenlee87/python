__author__ = "Steven Lee"


def test(*args):
    """
    *args：接收N个位置参数，比如1, 2, 3, 4, 5和*[1, 2, 3, 4, 5]
    """
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
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test2(name='steven', age='20', sex='male')  # print {'name': 'steven', 'age': '20', 'sex': 'male'}
test2(**{'name': 'stevenlee', 'age': 9, 'sex': 'male'})  # print{'name': 'stevenlee', 'age': 9, 'sex': 'male'}

print('------------')


def test3(name, age=18, **kwargs):
    print(name)
    print(age)
    print(kwargs)

test3('ste', 3, sex='male')
test3('ste', sex='male', age=20)
test3('steven')


def get_info(*args):
    print(args)

get_info('master/cpus_percent')