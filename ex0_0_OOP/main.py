from model.Drink import Drink
from model.DrinkVendingMachine import DrinkVendingMachine
from model.HotDrink import HotDrink

vodka = Drink("Vodka", 222, 500)
print(vodka)

vodka1 = Drink("Vodka", 222, 500)
print(vodka1)
print(vodka == vodka1)

hot_coffee = HotDrink("Coffee", 333, 0.2, 90)
hot_tea = HotDrink("Tea", 22, 0.2, 90)
print(hot_coffee)
print(hot_tea)
print(hot_tea == hot_coffee)

vending_machine = DrinkVendingMachine()
print(vending_machine)
vending_machine.add_product(vodka)
vending_machine.add_product(vodka1)
vending_machine.add_product(hot_tea)
vending_machine.add_product(hot_coffee)

print("Список продуктов в автомате....")
for p in vending_machine:  # iterable
    print(p)

print("Sorted Список продуктов в автомате....")
# vending_machine.sort(key=attrgetter('name'))
vending_machine.sort(lambda x: (x.cost))
vending_machine.print_all()

print("Ищем продукт....")
print(vending_machine.get_product("Vodka", 300))
print(vending_machine.get_product("Vodka", 500))
