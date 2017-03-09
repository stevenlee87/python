import json
__author__ = "Steven Lee"
# 序列化就是把内存的数据对象变成字符串


info = {
    "name": "stevenlee",
    "age": 20
}

# f = open("test.txt", "w")
# f.write(str(info))
# print(json.dumps(info))
# f.close()

f = open("test.txt", "w")
f.write(json.dumps(info))
f.close()
