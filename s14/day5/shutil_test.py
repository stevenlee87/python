import shutil
__author__ = "Steven Lee"

# shutil 模块：高级的文件、文件夹、压缩包 处理模块

# f1 = open("sys_test.py", encoding="utf-8")
# f2 = open("copy_sys_test.py", "w", encoding="utf-8")
# shutil.copyfileobj(f1, f2)

shutil.copyfile("sys_test.py", "copy_sys_test2.py")
