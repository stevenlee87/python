# Author:Steven Lee

import os

'''
import sys
print(sys.path)
print(sys.argv)
'''

# cmd_res = os.system("dir")  # 执行命令 不保存结果
cmd_res_mem = os.popen("dir")  # 执行命令 并保存内存对象
cmd_res = os.popen("dir").read()  # 执行命令 并保存结果
print("-->", cmd_res)

