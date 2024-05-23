import pygame
from obstacle import Obstacle
import random


class Wooden_box(Obstacle):
    '''
    Classe pour instancier l'obstacle caisse de bois

    Attributs:
    ---------

    image:Surface
        Charge l'image de la caisse de bois

    rect:RectType
        Donne le rectangle à l'image caisse en bois

    image: Surface.scale
        Redimension de l'image caisse en bois

    rect.x: int
        Définit la position en x de manière aléatoire

    rect.y: int
        Définit la position en y de manière aléatoire
    '''
    def __init__(self):
        '''
        Construit tous les attributs nécessaire au fonctionnement

        image:Surface
            Charge l'image de la caisse de bois

        rect:RectType
            Donne le rectangle à l'image caisse en bois

        image: Surface.scale
            Redimension de l'image caisse en bois

        rect.x: int
            Définit la position en x de manière aléatoire

        rect.y: int
            Définit la position en y de manière aléatoire
        '''
        super().__init__()
        self.image = pygame.image.load("Images/box.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = random.randint(150,800 )
        if self.rect.x in range(280,625):
            self.rect.x = random.randint(150,800)
        self.rect.y = random.randint(150,640)
        if self.rect.y in range(180, 480):
            self.rect.y = random.randint(150,640)