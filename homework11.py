# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.
import datetime


class BankAccount:
    balance = 0
    history = []

    @classmethod
    def replenish(cls, amount):
        cls.balance += amount
        time1 = datetime.datetime.now()
        cls.history.append(f'{time1}  На ваш баланс было зачисленно:{amount}')

        return f'На ваш баланс зачислено: {amount} '

    @classmethod
    def withdrawal(cls, amount_1):
        cls.balance -= amount_1
        time2 = datetime.datetime.now()
        cls.history.append(f'{time2}  С вашего баланса было списано: {amount_1}')

        return f'Вы сняли: {amount_1}'

    @classmethod
    def get_balance(cls):
        time3 = datetime.datetime.now()
        cls.history.append(f'{time3}  Была произведена проверка баланса, текущий баланс: {cls.balance}')
        return f'Остаток: {cls.balance}'


account_transactions = BankAccount()
account_transactions_1 = BankAccount()
print(account_transactions.replenish(300))
print(account_transactions.withdrawal(100))
print(account_transactions.get_balance())

print(account_transactions_1.replenish(400))
print(account_transactions_1.withdrawal(200))
print(account_transactions_1.get_balance())

print(*BankAccount.history)
