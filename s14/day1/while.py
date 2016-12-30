# Author:Steven Lee

age_of_steven = 20
count = 0

while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_steven:
        print("yes,you got it!")
        break
    elif guess_age > age_of_steven:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
else:
    print("you have tried many times!")
