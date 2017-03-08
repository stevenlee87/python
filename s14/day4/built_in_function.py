import functools
__author__ = "Steven Lee"

# Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
print(all([1, -1, 2]))  # print True
print(any([1, 0, -3]))
print(ascii([1, 2, "你好"]))  # 这个函数没什么用！
print(bin(255))  # 把一个整数由十进制转二进制

a = bytes("abcde", encoding="utf-8")  # 字串符不可以修改
b = bytearray("abcde", encoding="utf-8")  # bytearray 也很少用到！
print(a.capitalize(), a)
print(b[0], b[1])
b[1] = 100
print(b)


def sayhi():
    pass
print(callable(sayhi))

print(chr(97))  # 返回ascii 码的对应表 print a
print(ord('a'))  # print 97 与a丢应

# code = "for i in range(10):print(i)"
# c = compile(code, '', 'exec')  # compile 没有什么用！
# eval(c)  # 把一个字符串转换成一个字典

# (lambda n:print(n))(5)
# calc = lambda n:print(n)
# calc(5)

# res = filter(lambda n: n > 5, range(10))
# for i in res:
#     print(i)
#
# print("----map----")
# res = map(lambda n: n * n, range(10))
# for i in res:
#     print(i)

# import functools
res = functools.reduce(lambda x, y: x + y, range(10))  # 累加，打印从0加到9，等于45
print(res)

a = frozenset([1, 4, 333, 212])  # 不可变集合
print(globals())  # 打印整个程序所有的变量的key-value

print(hash('alex'))


def test():  # locals() 打印局部变量
    local_var = 333
    print(locals())
test()

print(oct(1))  # print 0o1,把数字转换成8进制
print(pow(3, 5))  # print 243,3的5次方
print(round(1.3342, 2))  # 保留两位

# sorted
d = {6: 2, 8: 0, 1: 4, -5: 6, 99: 11, 4: 22}
print(d)
print(sorted(d.items()))  # 按key来排序
print(sorted(d.items(), key=lambda x:x[1]))  # 按照value来排序

# zip 合并两个列表
list_a = [1, 2, 3, 4]
list_b = ['a', 'b', 'c', 'd', 'e']
for i in zip(list_a, list_b):
    print(i)
