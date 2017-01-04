__author__ = "Steven Lee"

# names = "Steven Lee Jack Bob"

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

names2 = names.copy()
print(names)
print(names2)
names[0] = "jerry"
print(names)
print(names2)