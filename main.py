from restaurant import Restaurant, Menu

m1 = Menu()
m1.set_menu(["Breakfast", "Lunch", "Happy Hour"], ["Soft Drinks", "Tea", "Coffee", "Alcohol"])
r1 = Restaurant("Jade Panda", 25, m1) 
r1.set_hours(7,21)
r1.summarize()


m2 = Menu()
m2.set_menu(["Breakfast", "Lunch"], ["Soft Drinks", "Tea", "Coffee", "Smoothies", "Juices"])
r2 = Restaurant("Bagel Bites", 10, m1) 
r2.set_hours(10,2)
r2.summarize()


