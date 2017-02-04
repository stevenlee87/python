__author__ = "Steven Lee"

music = "lemon tree"


def change_name(name):
    global music  # 全局变量，在函数外部也会生效，不建议使用！
    music = "California"
    print("before change", name, music)
    name = "Steven Lee"  # 局部变量，这个函数就是这个变量的作用域
    print("after change", name, music)

name = "steven"
change_name(name)
print("name is:", name)
print(music)
