class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.__balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено: {amount}")
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято: {amount}")
        else:
            print("Недостаточно средств или некорректная сумма")

    def get_balance(self):
        return self.__balance


Dastan = BankAccount("Dastan", 900)
print(Dastan.get_balance())
Dastan.deposite(100)
print(Dastan.get_balance())

Dastan.withdraw(100)
print(Dastan.get_balance())
Dastan.withdraw(901)
print(Dastan.get_balance())








