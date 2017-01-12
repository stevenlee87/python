import copy

__author__ = "Steven Lee"

# names = "Steven Lee Jack Bob"
'''
names = ["Stevenlee", "Lee", "Jack", "Bob"]

print("1,", names)  # ['Stevenlee', 'Lee', 'Jack', 'Bob']
print("2,", names[0])  # Stevenlee
print("3,", names[-2:])  # ['Jack', 'Bob']

names.append("Michael")
print("4,", names)  # ['Stevenlee', 'Lee', 'Jack', 'Bob', 'Michael']

names.insert(1, "Tom")  # 插入新字段
print("5,", names)  # ['Stevenlee', 'Tom', 'Lee', 'Jack', 'Bob', 'Michael']

# delete 3种方法
names.pop(2)  # or names.pop(-4)
# del names[2]
# names.remove("Lee")
print("6,", names)

print("7,", names.index("Stevenlee"))

names.append("Tom")
print("8,", names)

print("9,", names.count("Tom"))  # 查找列表中某个字串符的数量

names.reverse()
print("10,", names)  # 列表反转
'''

names = ["Stevenlee", "Lee", "Jack", "Bob", "jerry"]
print(names[:])
print(names[0:-1])  # print ['Stevenlee', 'Lee', 'Jack']
print(names[0:-1:2])
print(names[::2])


'''names = ["Stevenlee", "Lee", "Jack", "Bob", ["1", "2", "3"]]
# names2 = names.copy()  # shallow copy
# names2 = copy.copy(names)  # shallow copy
names2 = copy.deepcopy(names)  # deep copy
print(names)
print(names2)
names[0] = "jerry"
names[4][0] = "5"
print(names)
print(names2)
'''

person = ['name', ['saving', 100]]
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''
p1 = person[:]
p2 = person[:]

p1[0] = 'stevenlee'
p2[0] = 'jane'
print(p1)
print(p2)

a = [1, 2, 3]
b = a
a[1] = 555
print(a)
print("b is", b)

