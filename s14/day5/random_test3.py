import random
__author__ = "Steven Lee"

checkcode = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current != i:
        temp = chr(random.randint(65, 90))  # 大写的A-Z
    else:
        temp = random.randint(0, 9)
    checkcode += str(temp)
print(checkcode)
