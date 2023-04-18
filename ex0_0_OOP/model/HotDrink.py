from model.Drink import Drink


class HotDrink(Drink):

    def __init__(self, name: str, cost: float, volume: float, temperature: int):
        super().__init__(name, cost, volume)
        self.__temperature = temperature

    @property
    def temperature(self) -> int:
        return self.temperature

    @temperature.setter
    def temperature(self, temperature: int):
        self.__volume = volume

    def __str__(self) -> str:
        return f"HotDrink ({super().name}, cost= {super().cost}, volume= {super().volume},\
         Temperature= {self.__temperature})"

    def __eq__(self, o: object) -> bool:
        if (not isinstance(o, HotDrink)):
            return False;
        return super().__eq__(o) and \
            self.__temperature == o.temperature;

    # /**
    #  * Нагрев / охлаждение напитка
    #  *
    #  * @param temperature
    #  */
    def setTemperature(temperature: int):
        self.__temperature = temperature;
