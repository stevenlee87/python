__author__ = "Steven Lee"


def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print("-->", n)

calc(10)

# def calc(n):
#     """
#     递归最大次数是999次
#     """
#     print(n)
#     if int(n/2) == 0:
#         return n
#     return calc(int(n/2))
#
# calc(10)

# 递归函数必须有明确的结束条件
# 问题规模每递归一次都应该比上一次的问题规模减少
# 效率低
