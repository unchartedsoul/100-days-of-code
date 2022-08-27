
# import only system from os
from os import system, name


from art import logo
print(logo)
bids = {}
project = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")




def alpha():
    if name == 'nt':
      _ = system('cls')


while project:
  name = input("what is your name ")
  price= int(input('What"s your bid'))
  extend = input('Do someone else want to enter the bid').lower()
  bids[name] =price
  if extend == "no":
    project = False
    find_highest_bidder(bids)
  elif extend == "yes":
    alpha()


