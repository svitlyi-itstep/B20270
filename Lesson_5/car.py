'''

    Клас Car - мітує поведінку автомобіля

    ПОЛЯ:
    fuel - кількість палива у машини
    rate - витрати палива на 1 км
    traveled - скільки машина проїхала

    МЕТОДИ:
    drive - проїхати вказану відстань

'''

class Car:
    def __init__(self, fuel=0, rate=0.1):
        self.fuel = fuel
        self.rate = rate
        self.traveled = 0

    def __str__(self):
        return f'fuel: {self.fuel}\n' \
               f'rate: {self.rate}\n' \
               f'traveled: {self.traveled}\n'
    def drive(self, distance):
        if self.fuel < distance * self.rate:
            distance = round(self.fuel / self.rate, 3)
        self.traveled += distance
        self.fuel -= round(distance * self.rate, 1)
        return distance


