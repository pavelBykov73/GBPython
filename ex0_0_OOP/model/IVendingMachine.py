from model.Product import Product


class IVendingMachine:
    def __init__(self):
        pass

    def get_product(self, name: str) ->Product:
        pass

    def add_product(self, new_product: Product):
        pass
