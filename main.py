# coding=utf-8
"""
    Overview:
    - Prompt user to take action by displaying menu.
    - User has to purchase materials to enable the machine make the drink if the inserted coins reaches
      cost of the drink.
    - One can ask for report of items purchased.
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_items = MenuItem()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?\n{options}")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        my_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(coffee_maker.is_resource_sufficient(drink))
        print(drink)
