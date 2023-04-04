import random
def guess(x):
    randomNum=random.randint(1,x)
    guess= 0
    while guess!=randomNum:
        guess=int(input("enter a number: "))
        if guess>randomNum:
            print("too high, try again")
        elif guess<randomNum:
            print("too low, try again")
    print("yay you did it!")

guess(10)