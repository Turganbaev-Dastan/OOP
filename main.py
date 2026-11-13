# class Это структура данных,Которая служит для описания обектов
from traceback import print_tb


class Person:
    name: str = "Dastan"
    age: int = 15

    def sleep(self):
        print(f"{self.name} Спит ")

    def work(self):
        print(f"{self.name} работает")


person_1 = Person()

print(person_1.name)
print(person_1.age)
person_1.sleep()
person_1.work()

person_2 = Person()
person_2.name = "Aybek"
person_2.age = 31
print(person_2.name)
print(person_2.age)
person_2.sleep()
person_2.work()
