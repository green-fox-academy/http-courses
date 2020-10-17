from station import Station
from car import Car

station = Station(1000)

car = Car()
car.gas_amount = 50
station.refill(car)

print(car.gas_amount)
print(station.gas_amount)
