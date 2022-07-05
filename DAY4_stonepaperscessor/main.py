import random


r= rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s= scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
out = (r,p,s)
a= random.randint(0,2)
b= input("What does you chose?\n Type 0 for rock, 1 for paper and 2 for scissors")
A= int(a)
B =int(b)
print(f'Computer chosses {out[A]}')
print(f'You chosses is {out[B]}')


if B >= 3 or B < 0:
  print("You typed an invalid number, you lose!")
elif B == 0 and A == 2:
  print("You win!")
elif A == 0 and B == 2:
  print("You lose")
elif A > B:
  print("You lose")
elif B > A:
  print("You win!")
elif A ==B:
  print("It's a draw")