menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def money(drink_cost):
    """Check the coins user enerted and check weather it have enough money or not"""
    quater = int(input("how many quater?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))

    total = (quater * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if drink_cost< total:
        global profit
        profit += total
        change = round(total - int(drink_cost),2)
        print(f"Here is {change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def new_resources(user_input, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"here is your {user_input} enjoy")


while_continue = True

while while_continue:
    choice = input('What would you like ? (espresso/latte/cappuccino)')

    if choice == "report":
        print(resources)
    elif choice == "off":
        while_continue = False
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = money(drink["cost"])
            if payment:
                new_resources(choice, drink["ingredients"])
