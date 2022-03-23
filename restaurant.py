from enum import Enum
from typing import List

from people import Person

class DiningOptions(Enum):
    DINE_IN = 0
    DELIVERY = 1
    DRIVE_THROUGH = 2
    PICK_UP = 3

class Logistics:
    def __init__(self, basic_info):
        self.seats_available = 5
        self.num_staff = 3
        self.opening_hour = 0
        self.closing_hour = 23
        self.net_worth = 5000
        self.cost_level = 3
        self.cost_multiplier = 1
        self.dine_options = set()

    def change_num_staff(self, change_type):
        if change_type == 'hire':
            self.num_staff += 1
        else:
            self.num_staff -= 1
   
    def change_net_worth(self, profit_amt):
        self.net_worth += profit_amt 
    
    def set_hours(self, start, end):
        self.opening_hour = start if start < 12 else start-12
        self.closing_hour = end if end < 12 else end-12       

    def change_occupancy(self, seats):
        self.seats_available += seats

    def show_earnings(self):
        return self.net_worth

class Restaurant:
    def __init__(self, name, basics):
        self.restaurant_name = name
        self.logistics = Logistics(basics)
        self.menu = Menu()

    def show_earnings(self):
        return self.logistics.show_earnings()

    def summarize(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"Operating Hours {self.logistics.opening_hour}", "AM" if self.logistics.opening_hour < 12 else "PM",  "to ", f"{self.logistics.closing_hour}", "PM" if self.logistics.closing_hour < 12 else "PM" )
        self.menu.display_menu()

    def change_menu(self, item, item_type):
        if item_type == "food":
            self.menu.set_menu(item, [])
        else:
            self.menu.set_menu([], item)

    def check_menu(self, order_item):
        return order_item in self.menu.food or order_item in self.menu.drinks

    def process_order(self, order: str, people_involved: List[Person]) -> None:
            if self.check_menu(order):
                self.logistics.net_worth += 10
                for people in people_involved:
                    people.transact_order(10)
                

class Cafe(Restaurant):
    def __init__(self, name, basics):
        super().__init__(name, basics)
        food = ["cake", "muffin", "pie", "bread", "croissant", "danish"]
        drinks = ["coffee", "tea", "juice", "smoothies"]
        self.menu = Menu(food, drinks)
        self.logistics.dine_options = set([DiningOptions.DINE_IN, DiningOptions.PICK_UP, DiningOptions.DRIVE_THROUGH])
        self.logistics.cost_multipler = 0.8
    
class FastFood(Restaurant):
    def __init__(self, name, basics):
        super().__init__(name, basics)
        food = ["burger", "pizza", "sandwiches", "fries"]
        drinks = ["coffee", "tea", "juice", "smoothies", "soda"]
        self.menu = Menu(food, drinks)
        self.logistics.dine_options = set([DiningOptions.DINE_IN, DiningOptions.PICK_UP, DiningOptions.DRIVE_THROUGH, DiningOptions.DELIVERY])
        self.logistics.cost_multipler = 0.7

class Diner(Restaurant):
    def __init__(self, name, basics):
        super().__init__(name, basics)
        food = ["pasta", "burgers", "salads", "soups", "appetizer", "dessert"]
        drinks = ["coffee", "tea", "juice", "soda", "cocktail", "alcohol"]
        self.menu = Menu(food, drinks)
        self.logistics.dine_options = set([DiningOptions.DINE_IN, DiningOptions.PICK_UP, DiningOptions.DELIVERY])
        self.logistics.cost_multipler = 1.2

class FineDining(Restaurant):
    def __init__(self, name, basics):
        super().__init__(name, basics)
        food = ["Seafood", "pasta", "casseroles", "entrees", "appetizers"]
        drinks = ["coffee", "tea", "wine", "cocktail", "alcohol"]
        self.menu = Menu(food, drinks)
        self.logistics.dine_options = set([DiningOptions.DINE_IN])
        self.logistics.cost_multipler = 2.0

class Menu:
    def __init__(self, food=None, drinks=None):
        self.food = food if food is not None else set()
        self.drinks = drinks if drinks is not None else set()

    def set_menu(self, food_served, drinks_served):
        for food in food_served:
            self.food.add(food)
        for drink in drinks_served:
            self.drinks.add(drink)

    def display_menu(self):
        print("Food served:")
        for food in self.food:
            print("\t", food, end='')
        print("\n")

        print("Drinks served:")
        for drink in self.drinks:
            print("\t", drink, end='')
        print("\n")


