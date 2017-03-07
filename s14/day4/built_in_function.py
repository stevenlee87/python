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

code = "for i in range(10):print(i)"
c = compile(code, '', 'exec')  # compile 没有什么用！
eval(c)  # 把一个字符串转换成一个字典