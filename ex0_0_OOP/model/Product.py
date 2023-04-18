class Product:

    def __init__(self, name:str, cost:float):
        self.__name = name  # имя
        self.__cost = cost

    @property
    def name(self)->str:
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def cost(self)->float :
        return self.__cost

    @cost.setter
    def cost(self, cost:float):
        self.__cost = cost

    def display_info(self):
        print(f"Name: {self.__name} ")

    def __str__(self) -> str:
        return f"Product (name= {self.__name}, cost= {self.__cost})"

    def __eq__(self, o: object) -> bool:
        if (not isinstance(o, Product)) :
            return false;
        return self.__name.lower() == o.name.lower() and \
            self.__cost == o.cost
