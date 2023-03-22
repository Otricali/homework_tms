# 1
a, b = int(input('Введите а: ')), int(input('Введите b: '))

summ_res = a + b
subtract_res = a - b
multiplying_res = a * b
exponentiation_res = a ** b
modular_division_res = a % b
integer_division_res = a // b

print('Сумма = ', summ_res)
print('Разность = ', subtract_res)
print('Произведение = ', multiplying_res)
print('Возведение в степень = ', exponentiation_res)
print('Деление по модулю = ', modular_division_res)
print('Целочисленное деление = ', integer_division_res)

# 2
example1 = (((17 / 2) * 3) + 2)
print(example1)

example2 = (2 + ((17 / 2) * 3))
print(example2)

example3 = ((19 % 4) + ((15 / 2) * 3))
print(example3)

example4 = ((15 + 6) - (10 * 4))
print(example4)

example5 = (((17 / 2) % 2) * (3 ** 3))
print(example5)


# 3

x, y = int(input('введите х: ')), int(input('введите у: '))

expression_value = (abs(x) - abs(y)) / (1 + abs(x * y))
print("Результат: ", expression_value)
