import json
__author__ = "Steven Lee"
# 反序列化json.loads
# 反序列化 就是把字符串变成内存中的数据对象，方便读

f = open("test.txt", "r")

# data = eval(f.read())
# f.close()
# print(data['age'])

data = json.loads(f.read())
print(data['age'])
f.close()
