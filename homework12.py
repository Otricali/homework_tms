import datetime


class GetInfo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        time_call = datetime.datetime.now()
        result = self.func(*args, **kwargs)
        if args and kwargs:
            print(
                f'Функция get_sum вызвана в {time_call} с позиционными параметрами {args} и с именнованными параметрами {kwargs} ')
        elif args:
            print(f'Функция get_sum вызвана в {time_call} с позиционными параметрами {args}')
        elif kwargs:
            print(f'Функция get_sum вызвана в {time_call} с позиционными параметрами {kwargs}')
        else:
            print(f'Функция get_sum вызвана в {time_call} без пармаетров')
        return result


@GetInfo
def get_sum(a=0, b=0):
    res = a + b
    return res


get_sum(1, 2)
get_sum(1, b=3)
get_sum(a=1, b=3)
get_sum()
