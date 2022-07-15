import random
import art
from game_data import data

first_data = ''
second_data = ''

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def random_choice():
    selection = random.choice(list(data))
    return selection


def compare(a, b):
    if a > b:
        return 'A'
    elif a < b:
        return 'B'


def main():
    print(art.logo)
    score = 0
    first_data = random_choice()
    game_sholud_countinue = True
    while game_sholud_countinue:
        second_data = random_choice()
        print(f"Compare A: {format_data(first_data)}.")
        print(art.vs)
        print(f"Against B: {format_data(second_data)}.")
        user_input = input("type A for fist and B for second\n").capitalize()
        a = int(first_data["follower_count"])
        b = int(second_data['follower_count'])
        return_data = compare(a, b)
        if return_data == user_input:
            score += 1
            first_data = second_data
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_sholud_countinue  = False



main()
