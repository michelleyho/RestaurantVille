class Person:
    def __init__(self, fName, lName, bank_roll=None):
        self.first_name = fName 
        self.last_name = lName
        self.age = 18
        self.wallet = bank_roll if bank_roll is not None else 0
        self.salary = 0
        self.employer = []

    def credit(self, amt):
        self.wallet += amt
        print("Cha-ching!")

    def debit(self, amt):
        if self.check_wallet > 0:
            self.wallet -= amt
        else:
            print("Sorry.. out of money")

    def check_wallet(self):
        return self.wallet

    def transact_order(self, order_cost):
        raise NotImplementedError("Transact_order not implemented")

class Customer(Person):
    def transact_order(self, order_cost):
        self.wallet -= order_cost        

class Employee(Person):
   def get_job(self, employer, hourly_rate):
        self.employer.append(employer)
        self.salary = hourly_rate

   def hours_worked(self, amt):
        self.wallet = self.salary*amt

class FoodDelivery(Employee):
    def transact_order(self, order_cost):
        self.wallet += 0.3*order_cost 

class Server(Employee):
    def transact_order(self, order_cost):
        self.wallet += 0.25*order_cost

class Cook(Employee):
    pass
