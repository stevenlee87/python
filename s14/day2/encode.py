# -*- coding:gbk -*-
__author__ = "Steven Lee"

s = "���"

print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))

'''
pycharm���½��ļ���ʽҲ��GBK
b'\xc4\xe3\xba\xc3'
b'\xe4\xbd\xa0\xe5\xa5\xbd'
b'\xc4\xe3\xba\xc3'
'''