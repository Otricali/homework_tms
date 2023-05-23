# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.
import random


class Iterator:
    def __init__(self, start, end, stop=None):
        self.stop = stop
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        num = random.randint(self.start, self.end)
        if num == self.stop:
            raise StopIteration
        return num


def generator(start, end, stop=None):
    while True:
        num = random.randint(start, end)
        if num == stop:
            break
        yield num


try:
    for i in Iterator(0, 6, 1):
        print(i, end=' ''\n')
except StopIteration:
    print('stop')

try:
    for i in generator(0, 6, 1):
        print(i, end=' ')
except StopIteration:
    print('stop')
