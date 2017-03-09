import json
__author__ = "Steven Lee"
# 反序列化json.loads

f = open("test.txt", "r")

# data = eval(f.read())
# f.close()
# print(data['age'])

data = json.loads(f.read())
print(data['age'])
f.close()
