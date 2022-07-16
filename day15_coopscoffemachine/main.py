from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_maker.report()
money_machine.report()

while_continue = True

while while_continue:
    options = menu.get_items()
    choice = input(f'What would you like ? ({options})')

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        while_continue = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)
