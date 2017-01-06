__author__ = "Steven Lee"

name = "stevenlee is a \tgood boy!"
print(name.capitalize())
print(name.count("e"))
print(name.center(20, "-"))  # 打印20个字符，长度不够用-补足
print(name.endswith("ee"))  # 判断字符串以什么字符结尾，如果正确，输出True
print(name.expandtabs(tabsize=30))  # 改变\t的长度为30
print(name.find("e"))  # 查找字符从哪个index开始(从0开始)
print(name.find("is")) # name = "stevenlee is a \tgood boy!" print 10 空白算一个index