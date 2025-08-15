from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_maker = CoffeeMaker()
menu_items = Menu()
money_machine = MoneyMachine()

while machine_on:
    choice = input(f"What would you like? ({menu_items.get_items()}): ")

    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_items.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

