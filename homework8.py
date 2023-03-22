# 1
import csv
import json

string_1, string_2, string_3, string_4 = map(str, input('Введите 4 строки через пробел: ').split())
with open('text.txt', 'w') as file:
    file.write(string_1 + '\n' + string_2 + '\n')
with open('text.txt', 'a') as file:
    file.write(string_3 + '\n' + string_4)

# 2


dict_ = {111111: ('Joe', 19), 222222: ('Sam', 20), 333333: ('Frank', 44), 444444: ('Mark', 33), 555555: ('Jake', 27),
         666666: ('Ann', 23)}
with open('exampel.json', 'w') as file:
    json.dump(dict_, file, indent=4)

# 3


string_2 = []
string_3 = []
string_4 = [111, 222, 333, 444, 555, 666]

string_1 = ['Name', 'Age', 'Numbers']
with open('exampel.json', 'r+') as file:
    data_json = json.load(file)

keys_ = list(data_json.values())

for i, _ in enumerate(keys_):
    for i_1, _ in enumerate(keys_[i]):
        if i_1 % 2 == 0:
            string_2.append(keys_[i][i_1])
        else:
            string_3.append(keys_[i][i_1])

data = list(zip(string_2, string_3, string_4))
print(data)

with open('exampel1.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter=",", lineterminator="\r")
    csv_writer.writerow(string_1)
    csv_writer.writerow(data[0])
    csv_writer.writerow(data[1])
    csv_writer.writerow(data[2])
    csv_writer.writerow(data[3])
    csv_writer.writerow(data[4])
    csv_writer.writerow(data[5])


def get_sum(a, b):
    return a + b
