__author__ = "Steven Lee"


def is_float(s):
    '''
    这个函数是用来判断传入的是否为小数,包括正小数和负小数三
    :param s :传入一个字符串
    :return: True or False
    '''
    s = str(s)
    if s.isdigit():
        return False
    else:
        if s.count('.') == 1:  # 判断小数点个数
            sl = s.split('.')  # 分割字符串
            left = sl[0]  # 小数点前面的
            right = sl[1]  # 小数点后面的
            if left.startswith('-') and left.count('-') == 1 and right.isdigit():
                lleft = left.split('-')[1]  ##按照负号分割然后取负号后面的数
                if lleft.isdigit():
                    return True  # 负小数
                else:
                    return False
            elif left.isdigit() and right.isdigit():
                return True  # 正小数

            else:
                return False
        else:
            return False


print('-1.8 is :',is_float('-1.8'))
print('-s.8 is :',is_float('-s.8'))
print('-.8 is :',is_float('-.8'))
print('.8 is :',is_float('.8'))
print('-. is :',is_float('-.'))
print('1.4. is :',is_float('1.4'))

s2 = 1
s2 = str(s2)
float(s2)
print(type(s2))
