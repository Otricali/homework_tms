# 1 exercise

print('-------------------------------------------')
num = int(input('Введите число: '))
even_ = lambda x: x % 2 == 0
numbers = f'Четное: {num}' if even_(num) else f'Нечетное: {num}'
print(numbers)
print('-------------------------------------------')

# 2 exercise

import random
lst = [random.randint(1, 20) for _ in range(1, 20)]
print(list(map(lambda num: str(num), lst)))
print('-------------------------------------------')

# 3 exercise

tup_of_words = ('шабаш', 'шалаш', 'пиво',  'довод', 'доход')
print(tuple(filter(lambda word: word == word[::-1], tup_of_words)))
print('-------------------------------------------')

# 4 exercise

import time
from functools import wraps
from typing import Callable


def decorator(func: Callable) -> Callable:
    @wraps(func)
    def get_time(*args: int):
        time1 = time.time()
        result = func(*args)
        time2 = time.time()
        print(f'Время выполнения = {time2 - time1}')
        return result

    return get_time


@decorator
def get_quad(*args: int) -> list:
    lst = []
    for i in args:
        i *= i
        lst.append(i)
    return lst


print(f'Квадраты чисел: {get_quad(3, 4, 45, 34, 60, 66, 75, 7, 91, 40)}')
print('-------------------------------------------')

@decorator
def get_multiply(a: int, b: int) -> int:
    return a * b


print(f'Произведение чисел: {get_multiply(1000, 1000)}')
print('-------------------------------------------')


# 5 exercise


string = input('Введите число: ')



def get_info(value: str) -> str:
    if value.isdigit():
        value = int(value)
        return f'Вы ввели целое положительное число: {value}'
    elif value.count('-') == 1 and value[1::1].isdigit() and value.count('.') != 1:
        value = int(value)
        return f'Вы ввели цело отрицательное число : {value}'

    elif value.count('.') == 1 and value.count('-') != 1:
        var1 = value.replace('.', '')
        if var1.isdigit():
            value = float(value)
            return f'Вы ввели положительное дробное число: {value}'
        else:
            return f'Вы ввели некорректное число: {value}'

    elif value.count('.') == 1 and value.count('-') == 1:
        var1 = value.replace('.', '')
        if var1[1::1].isdigit() :
            value = float(value)
            return f'Вы ввели отрицательное дробное число: {value}'
        else:
            return f'Вы ввели некорректное число: {value}'
    else:
        return f'Вы ввели некорректное число: {value}'


print(get_info(string))


