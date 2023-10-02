import numpy as np


class House():
    """Описание дома"""
    def __init__(self, street, number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.age = 6
    def build(self):
        """Строит дом"""
        print("Дом на улице" + self.street + " Номер " + str(self.number) + " Построен")
    def age_of_hous(self, year):
        """возраст дома"""
        self.age += year
# House1 = House(" Murinsky", 34)
# House2 = House(" 1 Murinsky", 51)


# House1.age_of_hous(5)
# print(House1.age)
class prospecthouse(House):
    """Дома на проспектах"""
    def __init__(self,prospect,number):
        super().__init__(self, number)
        self.prospect = prospect
PrHouse = prospecthouse(" Проспект ленина ", 5)
print(PrHouse.prospect + str(PrHouse.number))
print(np.random.permutation(100))

