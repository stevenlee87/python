__author__ = "Steven Lee"

music = "lemon tree"
names = ["Steven", "Jack", "Bob"]


def change_name():
    names[0] = "Tom"  # 只有字符串和整数不能在局部里改变的。列表，字典在局部中可以修改。
    print("inside func", names)

change_name()
print(names)
