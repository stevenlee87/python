__author__ = "Steven Lee"

data = {
    'beijing': {
        'haidian': {
            'xierqi': ['baidu', 'qunar'],
            'wudaokou': ['sohu', 'kuaishou']
        },
        'chaoyang': {
            'wangjing': ['momo', '360']
        }
    },
    'shenzhen': {
        'nanshan': {
            'kejiyuan': ['tencent']
        },
        'longgang': {
            'longgang': ['huawei']
        }
    },
    'hangzhou': {
        'yuhang': {
            'wenyixilu': ['alibaba']
        }
    }
}

exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice = input("please input address1:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("please input address2:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("please input address3:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("Last level,please input b to return:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
    elif choice == "q":
        exit_flag = True