from model.Drink import Drink
from model.Product import Product
from model.VendingMachine import VendingMachine


class DrinkVendingMachine(VendingMachine):
    def __init__(self):
        super().__init__()

    def get_product(self, name: str, volume) -> Product:
        for product in super().__iter__():  # super().products:
            if isinstance(product, Drink) and product.name.lower() == name.lower() and product.volume == volume:
                return product;
        print(f"Продукт c названием {name} объемом {volume} не найден.")
        return None;

    # def add_product(self, new_product: Product):
    #     self.__products.append(new_product)
    #     super().add_product(new_product)

    def __str__(self) -> str:
        return "Drink Vending Machine"

    # def print_all(self):
    #     for product in self.__products:
    #         print(product)
    # 
    # def __iter__(self):
    #     return SimpleIterator(self.__products[:])
