__author__ = "Steven Lee"

# data = open('yesterday', encoding='utf-8').read()
# f = open('yesterday', 'r', encoding='utf-8')  # 文件句柄(文件的大小，文件的起始位置)
f = open('yesterday2', 'r+', encoding='utf-8')  # 文件句柄，读写，只会在文件的最后写入(常用!!!)
# f = open('yesterday2', 'w+', encoding='utf-8')  # 文件句柄，写读，只会在文件的最后写入
# f = open('yesterday2', 'a+', encoding='utf-8')  # 文件句柄，追加读写，只会在文件的最后写入
# f = open('yesterday2', 'rb')  # 文件句柄，二进制文件 (python3.0 只能用二进制模式传输，2.0还可以用字符传输)
# data = f.read()
# print(data)
# f.write("\nhello world!\n")
'''
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
'''

print(f.readline())
print(f.readline())
print(f.readline())
f.write("------------------good-------------------")

f.close()
