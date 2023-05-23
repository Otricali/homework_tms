# 1
import time


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


auto = Auto('Honda', 27, 'Civic', 'White', 950)
print(auto.brand)
auto.birthday()
print(auto.age)
auto.birthday()
print(auto.age)
print(auto.mark)
print(auto.color)
print(auto.weight)
auto.move()
auto.stop()


# 2

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print('move')
        print(f'Max speed is {self.max_speed}')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


auto_1 = Car('Honda', 27, 'Civic', 300, 'White', 950)
auto_2 = Car('BMW', 33, 'e30', 330, 'Black', 1500)
auto_3 = Truck('Ford', 3, 'F-150', 4000, 'Black', 2500)
auto_4 = Truck('Chevrolet', 25, 'Tahoe', 4500, 'Black', 3000)

print(auto_1.brand)
auto_1.birthday()
print(auto_1.age)
auto_1.birthday()
print(auto_1.age)
print(auto_1.mark)
print(auto_1.color)
print(auto_1.weight)
print(auto_1.max_speed)
auto_1.move()
auto_1.stop()
auto_1.load()
print('--------------')

print(auto_2.brand)
auto_2.birthday()
print(auto_2.age)
auto_2.birthday()
print(auto_2.age)
print(auto_2.mark)
print(auto_2.color)
print(auto_2.weight)
print(auto_2.max_speed)
auto_2.move()
auto_2.stop()
auto_2.load()
print('--------------')

print(auto_3.brand)
auto_3.birthday()
print(auto_3.age)
auto_3.birthday()
print(auto_3.age)
print(auto_3.mark)
print(auto_3.color)
print(auto_3.weight)
print(auto_3.max_load)
auto_3.move()
auto_3.stop()
auto_3.load()
print('--------------')

print(auto_4.brand)
auto_4.birthday()
print(auto_4.age)
auto_4.birthday()
print(auto_4.age)
print(auto_4.mark)
print(auto_4.color)
print(auto_4.weight)
print(auto_4.max_load)
auto_4.move()
auto_4.stop()
auto_4.load()
print('--------------')
