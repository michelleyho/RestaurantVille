from src.restaurant import *
from src.people import *


def test_restaurant_set_hours():
    r = Restaurant('Freddies Fish Fry')
    r.logistics.set_hours(9, 21)
    assert r.show_operating_hours() == '9AM-9PM'

def test_restaurant_transact_money():
    r = Restaurant('Freddies Fish Fry')
    r.transact_money(500)
    assert 5500 == r.show_earnings()

    r.transact_money(-800)
    assert 4700 == r.show_earnings()

def test_restaurant_change_menu_food():
    r = Restaurant('Freddies Fish Fry')
    r.change_menu(['calamari'], 'food')
    r.summarize()
    assert r.check_menu('calamari')

    r.change_menu(['hush_puppies', 'crab cakes'], 'food')
    assert r.check_menu('hush_puppies')
    assert r.check_menu('crab cakes')

def test_restaurant_change_menu_drink():
    r = Restaurant('Freddies Fish Fry')
    new_drinks = ['lemonade', 'sweet ice tea', 'ginger ale']
    r.change_menu(new_drinks, 'drinks')
    
    for new_drink in new_drinks:
        assert r.check_menu(new_drink)

def test_restaurant_change_staff():
    r = Restaurant("Busy Bee's")
    r.change_staff(5)
    
    assert r.logistics.num_staff == 8
    
    r.change_staff(-3)
    assert r.logistics.num_staff == 5

def test_restaurant_change_occupancy():
    r = Restaurant('Jade China')
    r.change_occupancy(5)
    assert r.show_available_seats() == 10

    r.change_occupancy(-8)
    assert r.show_available_seats() == 2

def test_restaurant_process_order():
    r = Restaurant('Pierre by the Pier')
    c = Customer('Nancy', 'Shmancy',100)
    r.change_menu(['Clam Chowder'], 'food')
    
    r.process_order('Clam Chowder',[c])
    
    assert 5010 == r.show_earnings()
    assert 90 == c.check_wallet() 

def test_fineDining():
    f = FineDining('Pierre by the Sea')
    assert f.check_menu('alcohol')
    assert DiningOptions.DELIVERY not in f.logistics.dine_options  

def test_diner():
    d = Diner("Dina's Diner")
    assert d.check_menu('salads')

def test_fastfood():
    f = FastFood("Berger's Burger")
    assert DiningOptions.DRIVE_THROUGH in f.logistics.dine_options
    assert f.check_menu('pizza')

def test_cafe():
    c = Cafe("Cathy's Corner")
    assert c.check_menu('croissant') 
