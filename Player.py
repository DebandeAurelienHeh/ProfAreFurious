from Vehicle import Vehicle
from Car import Car
from Tank import Tank
from Bike import Bike


class Player:
    def __init__(self, vehicle, inputs, pos=(200, 400)):
        self._vehicle = vehicle
        if self._vehicle == "Car":
            self._vehicle = Car(inputs, pos)
        elif self._vehicle == "Tank":
            self._vehicle = Tank(inputs, pos)
        elif self._vehicle == "Bike":
            self._vehicle = Bike(inputs, pos)

    @property
    def vehicle(self):
        return self._vehicle

    def update(self, screen, walls, powers, box):
        self.vehicle.update(screen, walls, powers, box)

    def show(self, screen):
        self.vehicle.show(screen)

    def collide(self, player, screen, box, powers, walls):
        self.vehicle.collide(player.vehicle, screen, box, powers, walls)
