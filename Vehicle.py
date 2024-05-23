import time
import pygame
import math
from heal import Heal
from speed import Speed
from push import Push

class Vehicle(pygame.sprite.Sprite):
    '''
        Classe servant à l'instanciation de Vehicule

        Attributs:
        ---------

        vect:math
            Vecteur pour la gestion des déplacements et des collisions

        inputs:()
                Tuples des touches pour jouer

        max_speed:int
            Valeur de vitesse maximale

        hp: int
            Valeur de vie du vehicule

        damage: int
            Montant de dégat que le vehicule inflige

        weight: int
            Poids du vehicule

        acceleration:int
            Calcul de l'acceleration

        sprite_name:str
            Nom de l'image correspondant

        scaling:float
            Sert au changement de la taille de l'image

        pos:()
            Tuples contenant les positions d'apparition

        Méthodes:
        --------

        show(screen= ecran)
            Sert à aficher les vehicules

        update(screen = ecran, walls= list, powers= list, box = list)
            Sert à la gestion des collisions et des interactions du vehicule

        rotate()
            Permet la gestion des dépalcement rotatif du vehicule

        vector_test(screen = ecran)
            Crée les lignes des vecteurs pour la gestion des vehicules

        collide(vehicule = Class, screen = ecran, box = list, powers = list, walls = list)
            Permet la gestion des collisions des vehicules

        loose_hp(vehicule = Class)
            Permet la perte de points de vie

        show_hp(screen = ecran)
            Permet l'affichage des points de vie

        game_over()
            Permet la gestion et déclenchement du Game Over
        '''
    vect = pygame.math.Vector2

    def __init__(self, max_speed, hp, damage, weight, acceleration, sprite_name, scaling, inputs, pos):
        pygame.sprite.Sprite.__init__(self)
        self._inputs = inputs
        if type(max_speed) == int:
            self._max_speed = max_speed
        else:
            self._max_speed = 10
        if type(hp) == int:
            self._hp = hp
        else:
            self._hp = 100
        if type(damage) == int:
            self._damage = damage
        else:
            self._damage = 10
        if type(weight) == int:
            self._weight = weight
        else:
            self._weight = 1
        if acceleration <= 1 or acceleration >= 0:
            self._acceleration = Vehicle.vect(0, -acceleration)
        else:
            self._acceleration = Vehicle.vect(0, -0.2)
        self._pos = pos
        self._angle = 0
        self._pressed = {}
        # Gère les images
        self._image = pygame.image.load("Images/" + sprite_name + ".png")  # pour choisir le sprite necessaire
        self._image = pygame.transform.scale_by(self._image, scaling)
        self._original_image = self._image
        self._rect = self._image.get_rect()
        self._speed = 0
        self._vel = Vehicle.vect(0, 0)
        self._angle_speed = 0
        self.font = pygame.font.Font(None, 36)
        self._timer = 0


    @property
    def pressed(self):
        return self._pressed

    @pressed.setter
    def pressed(self, value):
        self._pressed.append(value)

    def show(self, screen):
        '''
        Sert à aficher les vehicules
        Paramètre:
            screen =  Ecran

        Return:
            NONE
        '''
        screen.blit(self._image, self._rect)
        screen.blit(self._image, self._rect)

# update la position du vecteur de direction
    def update(self, screen, walls, powers, box):
        '''
        Sert à la gestion des collisions et des interactions du vehicule

        Paramètre:
            screen = ecran
            walls= list
            powers= list
            box = list

        Return:
            NONE
        '''
        self.show_hp(screen)
        if self._pressed.get(self._inputs[1]):
            self._angle_speed = -2
            self.rotate()
        if self._pressed.get(self._inputs[3]):
            self._angle_speed = 2
            self.rotate()
        if self._pressed.get(self._inputs[0]):
            self._vel += self._acceleration
        else:
            if self._vel.length() > 0.5:
                self._vel -= self._acceleration
            if not self._pressed.get(self._inputs[2]):
                self._vel = Vehicle.vect(0,0)
        if self._pressed.get(self._inputs[2]):
            self._vel -= self._acceleration

        # max speed
        if self._vel.length() > self._max_speed:
            self._vel.scale_to_length(self._max_speed)
        self._pos += self._vel
        self._rect.center = self._pos

        if self._pos.x < 30 or self._pos.x > 970:                 # si la voiture sort de l'écran, elle rebondit contre
            self._vel.x *= -1
        if self._pos.y < 30 or self._pos.y > 770:
            self._vel.y *= -1

        for wall in walls:                                        # collision avec les murs
            if self._rect.colliderect(wall):
                self._vel.x *= -1
                self._vel.y *= -1
                break

        if 380 <= self._pos.x <= 575 and 325 <= self._pos.y <= 485:     # Collision avec le centre
            self._vel.x *= -1
            self._vel.y *= -1

        for power_up in powers:
            for hitboxe in power_up:
                if self._rect.colliderect(hitboxe):
                    hitboxe.rect.x += 1000
                    if type(hitboxe) == Heal:
                        self._hp += 20
                    elif type(hitboxe) == Speed:
                        self._max_speed += 1

                    elif type(hitboxe) == Push:
                        print("push")

        if self._rect.colliderect(box):
            box.is_broken = True

        # Vehicle looses hp if in lava
        if self._pos.x < 50 or self._pos.x > 950:  # si la voiture sort de l'écran, elle revient à l'intérieur
            if self._timer % 5 == 0:
                self._hp -= 1
            else:
                pass

        if self._pos.y < 50 or self._pos.y > 750:
            if self._timer % 5 == 0:
                self._hp -= 1
            else:
                pass
        self._timer += 1

    def rotate(self):
        '''
        Permet la gestion des dépalcement rotatif du vehicule

        Paramètre:
            NONE

        Return:
            NONE
        '''
        # Rotate the acceleration vector.
        self._acceleration.rotate_ip(self._angle_speed)
        self._angle += self._angle_speed
        if self._angle > 360:
            self._angle -= 360
        elif self._angle < 0:
            self._angle += 360
        self._image = pygame.transform.rotate(self._original_image, -self._angle)
        self._rect = self._image.get_rect(center=self._rect.center)

    def vector_test(self, screen):
        '''
        Crée les lignes des vecteurs pour la gestion des vehicules

        Paramètre:
            screen = ecran

        Return:
            NONE
        '''
        pygame.draw.line(screen, "blue", (self._rect.center), (self._rect.center[0] + self._vel.x*10, self._rect.center[1] + self._vel.y*10))
        pygame.draw.line(screen, "red", (self._rect.center), (self._rect.center[0] + self._acceleration.x*100, self._rect.center[1] + self._acceleration.y*100))

    def collide(self, vehicle, screen, box, powers, walls):
        '''
        Permet la gestion des collisions des vehicules

        Paramètre:
            vehicule = Class
            screen = ecran, box = list
            powers = list
            walls = list

        Return:
            NONE
        '''
        if ((self._rect.center[0], self._rect.center[1]) + self._acceleration).distance_to(vehicle._rect.center) <= 50:
            vehicle._vel += self._vel * 7.5
            vehicle._pos += vehicle._vel
            vehicle.update(screen, box, powers, walls)
            vehicle.loose_hp(self)
            self._vel = -self._vel

    def loose_hp(self, vehicle):
        '''
        Permet la perte de points de vie

        Paramètre:
            Vehicule: Class

        Return:
            NONE
        '''
        self._hp -= vehicle._vel.length() * 2

    # HP RELATED FUNCTIONS
    def show_hp(self, screen):
        '''
        Permet l'affichage des points de vie

        Paramètre:
            screen = ecran

        Return:
            NONE
        '''
        text = self.font.render("HP: " + str(self._hp), True, (255, 255, 255))
        screen.blit(text, self._pos)
        if self._hp <= 0:
            game_over = self.font.render("GAME OVER", True, (255, 255, 255))
            screen.fill((0, 0, 0))

    def game_over(self):
        '''
        Permet la gestion et déclenchement du Game Over

        Paramètre:
            NONE

        Return:
            TRUE OR FALSE
        '''
        if self._hp <= 0:
            return True
        else:
            return False