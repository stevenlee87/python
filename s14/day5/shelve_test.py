import shelve
# import datetime
__author__ = "Steven Lee"
# shelve模块是一个简单的k,v, 将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式

d = shelve.open('shelve_test')  # 打开一个文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

# info = {'age': 22, 'job': 'it'}
# name = ["alex", "rain", "test"]
# d["name"] = name  # 持久化列表
# d["info"] = info  # 持久dict
# d['date'] = datetime.datetime.now()
# d.close()

# class Test(object):
#     def __init__(self, n):
#         self.n = n
#
# t = Test(123)
# t2 = Test(123334)
#
# name = ["alex", "rain", "test"]
# d["test"] = name  # 持久化列表
# d["t1"] = t  # 持久化类
# d["t2"] = t2
#
# d.close()
