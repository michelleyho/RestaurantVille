from restaurant import Cafe, FastFood, Diner, FineDining
from people import *

r1 = Diner("Jade Panda", 25) 
r1.logistics.set_hours(7,21)
print(r1.show_operating_hours())
r1.summarize()


r2 = Cafe("Bagel Bites", 10) 
r2.logistics.set_hours(10,2)
r2.summarize()


r3 = FineDining("Pierre by the Pier", 15)
r3.logistics.set_hours(17,21)
r3.summarize()

r4 = Diner("Freddy's Bistro", 40)
r4.summarize()
c4 = Customer("Sally", "Molly", 500)
s4 = Server("Jeeves", "Servantes", 100)
cook4 = Cook("Caty", "Kook", 100)
print("Before")
print(c4.check_wallet())
print(r4.show_earnings())
print(s4.check_wallet())
print(cook4.check_wallet())
r4.process_order("pasta", [c4, s4, cook4])
print("After")
print(c4.check_wallet())
print(r4.show_earnings())
print(s4.check_wallet())
print(cook4.check_wallet())


