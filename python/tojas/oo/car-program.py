from car import Car
from station import Station

station = Station()
car1 = Car()
car2 = Car()
car2.gas_amount = 20

station.refill(car1)
station.refill(car2)

print(station.gas_amount)
print(car1.gas_amount)
print(car2.gas_amount)
