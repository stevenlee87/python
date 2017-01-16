__author__ = "Steven Lee"

# data = open('yesterday', encoding='utf-8').read()
f = open('yesterday', 'r', encoding='utf-8')  # 文件句柄(文件的大小，文件的起始位置)
# f = open('yesterday2', 'a', encoding='utf-8')  # 文件句柄(文件的大小，文件的起始位置)
# data = f.read()
# print(data)
# f.write("\nhello world!\n")

print(f.tell())
print(f.readline()) # 可以指定读入的字符数
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())

print(f.encoding)
print(f.fileno())
# print(f.flush())  文件不是实时写入的，先执行f.write("hello\n")

f.close()
