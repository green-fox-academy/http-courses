class Station:
    def __init__(self, amount):
        self.gas_amount = amount
    def refill(self, car):
        self.gas_amount -= (car.capacity - car.gas_amount)
        car.gas_amount += (car.capacity - car.gas_amount)