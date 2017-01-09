__author__ = "Steven Lee"

name = "stevenlee is a \tgood boy!my name is {name},i am {year} years old."
print(name.capitalize())
print(name.count("e"))
print(name.center(20, "-"))  # 打印20个字符，长度不够用-补足
print(name.endswith("ee"))  # 判断字符串以什么字符结尾，如果正确，输出True
print(name.expandtabs(tabsize=30))  # 改变\t的长度为30
print(name.find("e"))  # 查找字符从哪个index开始(从0开始)
print(name.find("is"))  # name = "stevenlee is a \tgood boy!" print 10 空白算一个index
print(name[name.find("is"):])  # 字符串也可以切片
print(name.format(name="stevenlee", year=20))
print(name.format_map({'name': 'stevenlee', 'year': 20}))  # 格式化，format_map里面是个字典,key必须加引号
print('ab23'.isalnum())  # print True
print('_1A'.isidentifier())  # 判断是不是一个合法的标识符(变量名)
print(" ".isspace())  # print True
print("My Name Is".istitle())  # print True
print('MY NAME IS '.isupper())  # print True
print('+'.join(['1', '2', '3']))
print(name.ljust(100, '*'))
print(name.rjust(100, '-'))
print('StevenLee'.upper())  # 小写变成大写
print('STEVENLEE'.lower())  # 大写变成小写
print('\nSteven'.lstrip())
print('Steven\n'.rstrip())
print('    Steven\n'.strip())
print('---')

p = str.maketrans('abcdef', '123456')
print('steven'.translate(p))

print('steven lee'.replace('e', 'E', 1))  # 替换字符，只替换匹配到的第一个
print('steven lee2'.rfind('2'))  # 查找字符，返回对应的Index
print('1+2+3+4'.split('+'))  # 返回['1', '2', '3', '4']
print('Steven Lee'.swapcase())  # 大写变成小写，小写变成大写
