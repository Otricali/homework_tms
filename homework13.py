# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.
import random


class Iterator:
    def __init__(self, limit: int, stop_num):
        self.stop_num = stop_num
        self.limit = limit
        self.num = [random.randint(0, self.limit) for _ in range(0, 10)]

    def __getitem__(self, index: int):
        if self.stop_num == self.num[index]:
            raise StopIteration
        else:
            return self.num[index]


s_iter2 = Iterator(10, 1)
for i in s_iter2:
    print(i, end=' ')


def generator_function(limit: int, stop_num: int):
    index = 0
    while True:
        lst = [random.randint(0, limit) for _ in range(0, 10)]
        if lst[index] == stop_num:
            break
        else:
            index += 0
            yield lst[index]


for item in generator_function(10, 9):
    print(item)
