# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.
import datetime

history = []
balance = [0]


# replenish = [0]
# withdrawal = [0]


class BankAccount:
    i = 0
    i1 = 0

    def __init__(self, amount, amount_1):
        self.amount = amount
        self.amount_1 = amount_1

    def replenish(self):

        while self.i != 1:
            balance[0] = balance[0] + self.amount
            self.i += 1
        return f'На ваш баланс зачислено: {self.amount} '

    def withdrawal(self):

        while self.i1 != 1:
            balance[0] = balance[0] - self.amount_1
            self.i1 += 1
        return f'Вы сняли: {self.amount_1}'

    def get_balance(self):
        return f'Остаток: {balance[0]}'


class History(BankAccount):

    def hisory(self):
        super().replenish()
        vremya = datetime.datetime.now()
        super().withdrawal()
        vremya_1 = datetime.datetime.now()
        history.append(
            f'+{self.amount}, {vremya}. -{self.amount_1}, Время выполнения {vremya_1}.')

        return history


account_transactions = History(400, 100)
account_transactions_1 = History(400, 200)
print(account_transactions.replenish())
print(account_transactions.withdrawal())
print(account_transactions.get_balance())
print(*account_transactions.hisory())

print(account_transactions_1.replenish())
print(account_transactions_1.withdrawal())
print(account_transactions_1.get_balance())
print(*account_transactions_1.hisory())
