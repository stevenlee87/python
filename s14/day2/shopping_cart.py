__author__ = "Steven Lee"

goods_list = [["1", "iphone", "5800"], ["2", "mac", "12000"], ["3", "starbuck coffee", "31"], ["4", "python book", "81"]
    , ["5", "bike", "800"]]
goods_num = []
shopping_cart = []
salary = input("Please input your salary:")

while True:
    print("your account balance is ", salary)
    print("goods list is:", goods_list)

    buy = input("Please input which goods(number) you want to buy:")
    if str(buy) == "Q" or str(buy) == "q":
        print("Out of your shopping trip!")
        break
    for i in goods_list:
        if buy == i[0] and int(salary) > int(i[2]):
            shopping_cart.append(i)
            salary = int(salary)
            salary -= int(i[2])
            print("added {_goods} to you shopping cart!".format(_goods=i))
            continue
        else:
            print("Your balance is not enough to buy goods ", i)
            continue
