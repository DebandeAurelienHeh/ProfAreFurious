import pygame
from Vehicle import Vehicle
import random
class Tank(Vehicle):
    '''
    Classe servant à l'instanciation de Tank

    Attributs:
    ---------
    sprite_list:List
        Liste des différents tanks

    index: int
        Géneration aleatoire de l'index pour le choix du tank.

    Méthodes:
    --------

    attack()
        Rien d'implémenter

    shoot()
        Rien d'implémenter

    '''
    sprite_list = ["Tank_green", "tank_blue", "tank_pink"]

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

        self._index = random.randint(0, len(Tank.sprite_list)-1)
        super().__init__(3, 150, 40, 60, 0.2, Tank.sprite_list[self._index], 0.20, inputs, pos)


    def attack(self):
        '''
        Pas implémenter

        Return:
            NONE
        '''
        pass

    def shoot(self):
        '''
        Pas implémenter

        Return:
            NONE
                '''
        pass