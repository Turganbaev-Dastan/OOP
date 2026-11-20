class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод Vehicle")

class Car(Vehicle):
    def vehicle_method(self):
      print("Это из дочерного Класса")


class Cycle(Vehicle):
    def cycle_method(self):
        print("Этот метод из дочерного клааса cycle")

obj_c = Vehicle()
obj_c.vehicle_method()
obj_v = Car()
obj_v.vehicle_method()

obj_ccy = Cycle()
obj_ccy.cycle_method()
obj_ccy.vehicle_method()