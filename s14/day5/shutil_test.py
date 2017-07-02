import shutil
import zipfile
__author__ = "Steven Lee"

# shutil 模块：高级的文件、文件夹、压缩包 处理模块

# f1 = open("sys_test.py", encoding="utf-8")
# f2 = open("copy_sys_test.py", "w", encoding="utf-8")
# shutil.copyfileobj(f1, f2)

# shutil.copyfile("sys_test.py", "copy_sys_test2.py")

# shutil.copytree("a", "new_a")
# shutil.rmtree("new_a")

shutil.make_archive("shutil_archive_test", "zip", "D:\mydocuments\project\python\s14\day1")

z = zipfile.ZipFile("day1.zip", "w")
z.write("p_test.py")
print("------")
z.write("shelve_test.py")
z.close()
