# Задание 1
print('')

a = 1
b = 1
c = 1
print(id(a), id(b), id(c))

print('-------------------------')

# Задание 2

num1 = {1000.0, 2, 'hello'}
num2 = {1000.0, 2, 'hello'}
print(id(num1), id(num2))

print('-------------------------')

# Задание 3

tuple_ = (1, 2, 3)

_, number_1, _ = tuple_
_, _, number_2 = tuple_
number_3, _, _ = tuple_
print(number_1, number_2, number_3)

print('-------------------------')

# Задание 4

countries_capitals = {
    'Belarus': 'Minsk',
    'Poland': 'Warsaw',
    'Great Britain': 'London',
}
print(countries_capitals['Poland'])
print(countries_capitals['Belarus'])

print('-------------------------')

# Задание 5

food = ['котлета', 'пюрешка', 'драники', 'пицца', 'мороженное']
print(f'Из предлженного я больше люблю {food[0]} и {food[1]}')

print('-------------------------')

# Задание 6

friends = ['Egor', 'Liza', 'Vanya', 'Yana']

name = input('Введите имя: ')

if name in friends:
    print(f'У меня есть друг {name}')
else:
    print(f'У меня нет друга с именем {name}')
