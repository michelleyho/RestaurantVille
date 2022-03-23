class Restaurant:
    def __init__(self, name, num_seats, menu):
        self.restaurant_name = name
        self.seats_available = num_seats
        self.num_staff = 3
        self.menu = menu
        self.opening_hour = 0
        self.closing_hour = 23
        self.net_worth = 5000

    def set_hours(self, start, end):
        self.opening_hour = start if start < 12 else start-12
        self.closing_hour = end if end < 12 else end-12       

    def summarize(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"Operating Hours {self.opening_hour}", "AM" if self.opening_hour < 12 else "PM",  "to ", f"{self.closing_hour}", "PM" if self.closing_hour < 12 else "PM" )
        self.menu.display_menu()

    def change_num_staff(self, change_type):
        if change_type == 'hire':
            self.num_staff += 1
        else:
            self.num_staff -= 1

class Menu:
    def __init__(self):
        self.meals = set()
        self.drinks = set()

    def set_menu(self, meals_served, drinks_served):
        for meal in meals_served:
            self.meals.add(meal)
        for drink in drinks_served:
            self.drinks.add(drink)

    def display_menu(self):
        print("Meals served:")
        for meal in self.meals:
            print("\t", meal, end='')
        print("\n")

        print("Drinks served:")
        for drink in self.drinks:
            print("\t", drink, end='')
        print("\n")


