import random

from pyglet.image.codecs.s3tc import decode_dxt3


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]


    def move(self, x, y, z):
        d = self.speed
        dx = d*x
        dy = d*y
        dz = d*z
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
           self._cords = [dx, dy, dz]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]} , Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        return

class  Bird(Animal):
    beak = True

    def lay_eggs(self):
        # random.randint(1, 4) - вывод случайного числа от 1 до 4
        print("Here are(is)",  random.randint(1, 4), "eggs for you")

class AquaticAnimal(Animal):


    def dive_in(self, z):

        self._cords[2] -=  int(abs(z) * self.speed/2) # self._cords[2] = dz, [а -= в] то же самое, что и [a = a-b],
        # dz = z*d, d - скорость, уменьшаем dz на это значение

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()


db.lay_eggs()


