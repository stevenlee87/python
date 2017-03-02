__author__ = "Steven Lee"

# a, b = b, a + b
# 相当于：
# t = (b, a + b)
# a = t[0]
# b = t[1]


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        # print(b)
        yield b  # 返回当前状态的值
        a, b = b, a + b
        n += 1
    return "----done----"

# fib(10)
# print(fib(10))

# print(f.__next__())  # print 1
# print(f.__next__())  # print 1
# print(f.__next__())  # print 2

f = fib(5)
while True:
    try:
        x = next(f)  # 内置方法
        print("f:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
