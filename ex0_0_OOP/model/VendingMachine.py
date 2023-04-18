from model.IVendingMachine import IVendingMachine
from model.Product import Product


class VendingMachine(IVendingMachine):
    def __init__(self):
        self.__products = []  #:Product
        self.__index = 0

    @property
    def products(self) -> list:
        return self.__products

    def get_product(self, name: str) -> Product:
        for product in self.__products:
            if isinstance(product, Product) and product.name.lower() == name.lower():
                return product;
        print(f"Продукт c названием {name} не найден.")
        return None;

    def add_product(self, new_product: Product):
        if (self.products.count(new_product) == 0):
            self.__products.append(new_product)

    #        super().add_product(new_product)

    def __str__(self) -> str:
        return "Vending Machine"

    def print_all(self):
        for product in self.__products:
            print(product)

    def __iter__(self):
        return SimpleIterator(self.__products[:])

    def sort(self, sort_key):
        self.products.sort(key=sort_key, reverse=False)


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, product_list: list):
        self.products = product_list
        self.limit = len(product_list)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.products[self.counter - 1]
        else:
            raise StopIteration
