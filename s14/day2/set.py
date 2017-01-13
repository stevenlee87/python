__author__ = "Steven Lee"

list_1 = [1, 4, 5, 7, 3, 6, 7, 9, 8, 2]
# list_1 = ['1', '2']
list_1 = set(list_1)  # 集合也是无序的！！
print(list_1, type(list_1))  # print {1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>

list_2 = {2, 66, 0, 88, 6}
# list_2 = ['2', '66', '0', '88', '6']
print(list_1.intersection(list_2))  # 交集
print(list_1.union(list_2))  # 并集
print(list_1.difference(list_2))  # 差集 in list_1 not in list_2 ,前提是list_1必须是一个集合，不然会报错!!!
print(list_2.difference(list_1))  # 差集 in list_2 not in list_1 ,前提是list_2必须是一个集合，不然会报错!!!

# 子集
list_3 = {1, 3, 7}
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))

# 对称差集
print(list_1.symmetric_difference(list_2))

print("-------------------")
list_4 = {2, 4, 6}
print(list_3.isdisjoint(list_4))

# 交集
print(list_1 & list_2)
# 并集 union
print(list_1 | list_2)
# difference
print(list_1 - list_2)  # in list_1 not in list_2
print(list_2 - list_1)  # in list_2 not in list_1
# 对称差集
print(list_1 ^ list_2)  # 取两个集合中相互都没有的

list_1.add(999)
list_1.update([888, 999])
print(list_1)

list_5 = {2, 66, 0, 88, 6}
type(list_5)
print(type(list_5))

print(list_1)
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
list_1.discard('ddd')  # 集合中没有这个元素也不会报错，会打印None
