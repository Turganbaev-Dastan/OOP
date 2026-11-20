class Person:
    def __init__(self):
        self.name = "Dastan"
        self.__password = "042811"
        self._year = 2000

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

obj = Person()
print(obj.name)
print(obj._year)
print(obj.get_password())