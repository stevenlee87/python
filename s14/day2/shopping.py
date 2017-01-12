__author__ = "Steven Lee"

goods_list = [
    ("iphone", 5800),
    ("mac", 12000),
    ("coffee", 31),
    ("bike", 800),
    ("python book", 120)
]

shopping_list = []

salary = input("Please input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        print("your current balance is: \033[31;1m%s\033[0m" % salary)
        print("-----------shopping list------------")
        # enumerate(iterable[, start]) -> iterator for index, value of iterable
        for index, item in enumerate(goods_list):
            print(index, item)

        user_choice = input("Please input which goods you want to buy:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(goods_list) and user_choice >= 0:
                p_item = goods_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, your current balance is:\033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("\033[41;1mYour balance is: %s, not enough to buy goods:%s\033[0m" % (salary, p_item))
            else:
                print("\033[41;1mproduct code %s is not exist!\033[0m" % user_choice)
        elif user_choice == "q" or user_choice == "Q":
            print("-----------your shopping cart------------")
            for p in shopping_list:
                print(p)
            print("you current balance is: \033[31;1m%s\033[0m" % salary)
            exit()
        else:
            print("input error!")
