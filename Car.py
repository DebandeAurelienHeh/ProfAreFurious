import pygame
from Vehicle import Vehicle
import random

class Car(Vehicle):
    '''
        Classe servant à l'instanciation de Car

        Attributs:
        ---------
        sprite_list:List
            Liste des différents car

        index: int
            Géneration aleatoire de l'index pour le choix du car.

        Méthodes:
        --------

        attack()
            Rien d'implémenter


        '''
    sprite_list = ["car"]
    def __init__(self, inputs, pos):
        '''

        Construit les attributs necessaire au fonctionnement
        Paramètres:
            inputs:()
                Tuples des touches pour jouer
            pos:()
                Tuples contenant les positions d'apparition
            index: int
                Géneration aleatoire de l'index pour le choix du tank.
                '''
        self._index = random.randint(0, len(Car.sprite_list)-1)
        super().__init__(5, 100, 10, 30, 0.3, Car.sprite_list[self._index], 0.10, inputs, pos)

    def attack(self):
        '''
        Pas implémenter

        Return:
            NONE
        '''
        pass
