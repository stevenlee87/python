__author__ = "Steven Lee"

with open("yesterday2", "r", encoding="utf-8") as f:  # 也可以打开多个文件
    for line in f:
        print(line)
