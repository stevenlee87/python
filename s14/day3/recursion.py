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
