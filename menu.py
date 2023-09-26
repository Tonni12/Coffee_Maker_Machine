# coding=utf-8
"""
    :
"""

class MenuItem:
    """
    Models each menu item
    """
    def __int__(self, name, cost, milk, ingredients, water, sugar):
        self.name = name
        self.cost = cost
        self.ingredients = {'water': water,
                            'milk': milk,
                            'sugar': sugar
                            }

class Menu:
    """
            Models each Menu Item
        """
    def __init__(self):
        self.menu = [
              #  MenuItem(name='latte', water=300, milk=500, sugar=45, coffee=35, cost=12.5),
              #  MenuItem(name='lip tea', water=650, milk=500, sugar=15, lip_tea=250, cost=9.5),
              #  MenuItem(name='coffee', water=350, milk=56, sugar=25, coffee=23, cost=10)
           ]
    def get_items(self):
            """
        :return: Returns alll the names of the available menu items
        """
            choice = ""
            for item in self.menu:
                choice += f"{item.name}\t"
            return choice

    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by name. Returns all items if it exists and None otherwise.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, item not found! Try another keyword.")