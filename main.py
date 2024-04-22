class Electric:
    def __init__(self):
        self.__battery = 0

    def charge(self):
        self.__battery = 100


class Vehicle:
    pass


class ElectricCar(Vehicle, Electric):
    pass


class ElectricMoto(Vehicle, Electric):
    pass


car = ElectricCar()
moto = ElectricMoto()

print("ElectricCar MRO:", ElectricCar.mro())
print("ElectricMoto MRO:", ElectricMoto.mro())

car.charge()
moto.charge()

print("ElectricCar battery:", car._Electric__battery)
print("ElectricMoto battery:", moto._Electric__battery)
