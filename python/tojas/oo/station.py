class Station:
    def __init__(self):
        self.gas_amount = 1000

    def refill(self, car):
        gas_need = car.capacity - car.gas_amount
        car.gas_amount += gas_need
        self.gas_amount -= gas_need