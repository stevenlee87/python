import os
import time
__author__ = "Steven Lee"

os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
# os.chdir(r"c:\\Users")
# os.chdir(r"d:\project")  # r 用于转义
print(os.curdir)  # 返回当前目录: ('.')
print(os.pardir)  # 获取当前目录的父目录字符串名：('..')
# os.makedirs('dirname1/dirname2')  # 可生成多层递归目录
# os.makedirs(r"c:\a\b\c\d")
# os.removedirs('dirname1')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.removedirs(r"c:\a\b\c\d")
# os.mkdir('dirname')  # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove('spam.log')  # 删除一个文件
# os.rename("oldname", "newname")  # 重命名文件/目录
# os.stat('path/filename')  # 获取文件/目录信息
print(os.sep)  # print \ 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.linesep)  # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print("---")
print(os.pathsep)  # 输出用于分割文件路径的字符串
print(os.name)  # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")  运行shell命令，直接显示
print(os.environ)  # 获取系统环境变量
print(os.path.abspath(r'd:\project\python\README.md'))  # 返回path规范化的绝对路径
print(os.path.split(r'd:\project\python\README.md'))  # 将path分割成目录和文件名二元组返回
print(os.path.dirname(r'd:\project\python\README.md'))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(r'd:\project\python\README.md'))  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists(r'd:\project\python\README.md'))  # 如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs(r'project\python\README.md'))  # 如果path是绝对路径，返回True
print(os.path.isfile(r'd:\project\python\README.md'))  # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir(r'd:\project\python'))  # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime(r'd:\project\python\README.md'))  # 返回path所指向的文件或者目录的最后存取时间 print timestamp
x = os.path.getatime(r'd:\project\python\README.md')
print(time.ctime(x))  # print Thu Jan  5 11:46:15 2017
print(os.path.getmtime(r'd:\project\python\README.md'))  # 返回path所指向的文件或者目录的最后修改时间
y = os.path.getmtime(r'd:\project\python\README.md')
print(time.ctime(y))
