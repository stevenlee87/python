# Author:Steven Lee

age_of_steven = 20
guess_age = int(input("guess age:"))

if guess_age == age_of_steven:
    print("yes,you got it!")
elif guess_age > age_of_steven:
    print("think smaller...")
else:
    print("think bigger!")
