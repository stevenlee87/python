# Author:Steven Lee

import os


for i in range(3):
    username = input("your username:")
    password = input("your password:")
    if os.stat("lock.txt").st_size == 0:
        pass
    else:
        with open("lock.txt", "r") as f:
                content = f.read()
                content = content.split()
                if username == content[0]:
                    print("your account have locked!")
                    break
    with open("auth.txt", "r") as f:
        content = f.read()
        content = content.split()
        if username == content[0] and password == content[1]:
            print("hello!welcome to login our website!")
            break
        elif username == content[0] and password != content[1]:
            print("password mistake!")
        else:
            print("The username and password mistake")
else:
    print("you have tried many times,your acount will be locked!")
    with open("lock.txt", 'a') as f:
        f.write('{_username} locked'.format(_username = username))
