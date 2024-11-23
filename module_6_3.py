class Animal:
    def __init__(self, speed):
        self.speed = speed

    _cords = []
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def move(self, x, y, z):
        d = self.speed
        self._cords[0] = d * x
        self._cords[1] = d * y
        self._cords[2] = d * z

    def get_cords(self, dx, dy, dz):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]} , Z: {self._cords[2]}")

    def attack(self):
        if _DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif _DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        return


class Bird(Animal):
    beak = True

    def lay_eggs(self, egg):
        print(f"Here are(is) {self.egg} eggs for you")


class AquaticAnimal(Animal):
    super().__init__(speed)

    def dive_in(self, z):
        abs(z) * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    super().__init__(speed)


class Duckbill(Animal, AquaticAnimal, Bird, PoisonousAnimal):
    super().__init__(speed=1)
    sound = "Click-click-click"
    super().dive_in(z)


print(Duckbill.mro())