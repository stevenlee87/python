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

while True:
    for i in data:
        print(i)

    choice = input("please input address1:")
    if choice in data:
        while True:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("please input address2:")
            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("please input address3:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("Last level,please input b to return:")
                        if choice4 == "b":
                            pass
                    if choice3 == "b":
                        break
            if choice2 == "b":
                break