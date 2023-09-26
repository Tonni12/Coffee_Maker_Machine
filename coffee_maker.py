# coding=utf-8
"""
    Models the machine that makes the particular drink.
"""
class CoffeeMaker:
    """
    Models the machine that makes the machine
    """
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk": 450,
            "coffee": 50,
            "sugar": 250
        }

    def report(self):
        """
        Displays the report of all resources.
        :return:
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Sugar: {self.resources['sugar']}mg")

    def is_resource_sufficient(self, drink):
        """
        Returns True if ordered drink can be made else False
        :param drink:
        :return: Boolean value
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there isn't enough {item}.")
            can_make = False
        return can_make

    def make_coffee(self, order):
        """
        Deducts required ingredients from the resources available.
        :param order:
        :return:
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Your order, {order.name} is ready. Enjoy!")