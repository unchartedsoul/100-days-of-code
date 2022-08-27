print('Welcome to the tip calculator')
total_bill = int(input('What is the bill?'))
tip = int(input('what percentage tip would yo like to give? 10, 12 or 15'))
people = int(input('How many people to split the bill?'))
total_tip = round((total_bill/people)*(tip/100) +(total_bill/people), 2)

print(f"Each person should pay: ${total_tip}")
