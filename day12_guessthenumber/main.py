import random
import art

difficulty_hard =5
difficulty_easy = 10

def set_difficulty():

    a = input('type e for easy and h for hard').lower()
    if a == "h":
        return difficulty_hard
    elif a == "e":
        return difficulty_easy

def check(ans, num, level):
    i = ans
    if i == num:
        print('You won!!!')
    elif i < num:
        print('Try Higher \n try again')
        level -= 1
    elif i > num:
        print('Try Lower \n try again')
        level -= 1
    return level



def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    num = random.randint(1, 100)
    level = set_difficulty()
    ans = 0
    while ans != num:
        ans = int(input("enter your guess"))
        level = check(ans,num,level)

        if level == 0:
            print(level)
            print("You've run out of guesses, you lose.")
            break




game()
