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

print(info)
info['stu1101'] = '杰克'
print(info['stu1101'])
# del info['stu1101']
# print(info)

# info.pop('stu1101')  # 删除key
# print(info)

info.popitem()  # 随即删除
print(info)
