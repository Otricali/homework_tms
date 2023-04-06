# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.
import random


class Iterator:
    def __init__(self, start, end, stop):
        self.stop = stop
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        num = random.randint(self.start, self.end)
        if num == self.stop:
            raise StopIteration
        else:
            return num


def generator(start, end, stop):

    while True:
        num = random.randint(start, end)
        if num != stop:
            yield num
        else:
            break


iterator = Iterator(0, 6, 1)
try:
    for i in range(5):
        print(next(iterator), end=' ')
except StopIteration:
    print('stop')

gen = generator(0, 6, 1)
try:
    for i in range(5):
        print(next(gen), end=' ''\n')
except StopIteration:
    print('stop')
