# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

import datetime
from functools import wraps
from typing import Callable


def decorator(func: Callable) -> Callable:
    @wraps(func)
    def get_info(*args: int, **kwargs: int):
        lst = [f'Функция {func.__name__} вызвана {datetime.datetime.now()}']
        result = func(*args, **kwargs)
        if args and kwargs:
            lst.append(f'с позиционными параметрами {args} и с именнованными параметрами {kwargs}')
        elif args:
            lst.append(f'с позиционными параметрами {args}')
        elif kwargs:
            lst.append(f'с позиционными параметрами {kwargs}')
        else:
            lst.append('без пармаетров')

        print(*lst)
        return result

    return get_info


@decorator
def get_sum(a=0, b=0) -> int:
    return a + b


get_sum(1,3)
get_sum(a=1,b=3)
get_sum(1,b=3)
get_sum()

