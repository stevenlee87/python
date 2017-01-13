__author__ = "Steven Lee"

# data = open('yesterday', encoding='utf-8').read()
f = open('yesterday', encoding='utf-8')  # 文件句柄(文件的大小，文件的起始位置)
f.readlines()

f.close()
