from model.Product import Product


class Drink(Product):

    def __init__(self, name:str, cost:float, volume:float):
        super().__init__(name, cost)
        self.__volume = volume

    @property
    def volume(self) -> float:
        return self.__volume

    @volume.setter
    def volume(self, volume:float):
        self.__volume = volume

    def __str__(self) -> str:
        return f"Drink (name= {super().name}, cost= {super().cost}, volume= {self.__volume})"

    def __eq__(self, o: object) -> bool:
        if (not isinstance(o, Drink)) :
            return false;
        return  super().__eq__(o) and \
            self.__volume == o.volume;

