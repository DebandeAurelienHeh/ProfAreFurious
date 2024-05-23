import pygame
from Vehicle import Vehicle
import random

class Bike(Vehicle):
    '''
        Classe servant à l'instanciation de Bike

        Attributs:
        ---------
        sprite_list:List
            Liste des différents bike

        index: int
            Géneration aleatoire de l'index pour le choix du bike.

        Méthodes:
        --------

        jump()
            Rien d'implémenter

        '''
    sprite_list = ["Bike"]
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
        self._index = random.randint(0, len(Bike.sprite_list)-1)
        super().__init__(4.5, 10, 1, 1, 0.1, Bike.sprite_list[self._index], 0.10, inputs, pos)

    def jump(self):
        '''
        Pas implémenter

        Return:
            NONE
        '''
        pass