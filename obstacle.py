import pygame

class Obstacle:
    '''
    Classe abstraite Obstacle

    Attributs:
    ---------

    is_broken: bool
        Définit si l'obstacle à une un collision afin de le refaire apparatire
    '''
    def __init__(self):
        '''
        Construit tous les attributs nécessaire au fonctionnement

        is_broken: bool
            Définit si l'obstacle à une un collision afin de le refaire apparatire
        '''
        self.is_broken = False




