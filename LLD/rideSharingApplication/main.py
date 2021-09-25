from person import Driver, Rider
from system import System

# if __name__ == "__main__":
#     r1 = Rider(1, "Ankit")
#     d1 = Driver("Ram Bahadur")
#
#     r2 = Rider(2, "Jony")
#     r3 = Rider(3,"Sabastian")
#
#     riders = []
#     riders.append(r1)
#     riders.append(r2)
#     riders.append(r3)
#
#     r1._create_ride(50, 60,1, 1)
#     print(r1._close_ride())
#
#     s = System(3, riders)
#     s.create_ride(1,1, 50, 60,1)
#     print(s.close_ride(1))


class abc:
    def __init__(self):
        self.a = 1
        self._a = 11
        self.__aa = 12

    def b(self):
        print("a")

    def _b(self):
        print("_b")

    def __b(self):
        print("__b")


t = abc()
print(t.a)
print(t._a)
# print(t.__aa)
t.b()
t._b()
t.__b()
