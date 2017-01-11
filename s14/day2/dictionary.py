__author__ = "Steven Lee"

info = {
    'stu1101': 'jack li',
    'stu1102': 'bob wang',
    'stu1103': 'Tom lu',
    'stu1104': 'jerry',
    'stu1105': 'tim',
    'stu1106': 'john',
    'stu1107': 'jane',
}

# 增
info['stu1108'] = 'howard'
print(info)

# 删
print(info['stu1101'])
# del info['stu1101']
# print(info)

# info.pop('stu1101')  # 删除key
# print(info)

info.popitem()  # 随机删除，但是我测试是删除最后一个key
print(info)

# 改
print(info)
info['stu1101'] = '杰克'

# 查
print(info['stu1101'])  # 这种查找方式必须确定key存在才可以用
print(info.get('stu1109'))
print('stu1101' in info)  # print True    info.has_key('stu1101') in py2.x

# 打印所有值
print(info.values())

# 打印所有key
print(info.keys())

# 多级操作
info_key_list = {
    'chinese': {
        'www.baidu.com': ['chinese search engine', 'Good for Chinese search']
    },
    'english': {
        'www.google.com': ['american search engine', 'Good for Chinese search']
    }
}

info_key_list['chinese']['www.baidu.com'][1] = 'Good for world'
info_key_list.setdefault("taiwan", {"www.ksearch.com": ['1', '2']})  # 先去字段中取key的值，如果能取到，就把key的值返回，如果取不到就创建一个对应的值
print(info_key_list['chinese'])
print(info_key_list)

b = {
    'stu1101': 'steven',
    '1': '5',
    '2': '6'
}
info.update(b)
print(info)

