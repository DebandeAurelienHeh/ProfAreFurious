import pygame
import random

class Speed(pygame.sprite.Sprite):
    '''
        Classe de création de Speed

        Attributs:
        ---------
        image: Surface
            Chargement de l'image de Speed

        image: Surface scale
            Redimension de l'image de Speed

        rect: RectType
            Mise d'un rectangle pour les collisions autour de l'image Speed

        rect.x:int
            Génération de la postion de l'image sur l'axe des x de manière aléatoire

        rect.y:int
            Génération de la postion de l'image sur l'axe des y de manière aléatoire
        '''
    def __init__(self):
        '''
        Construit tous les attributs nécessaire au fonctionnement

        image: Surface
            Chargement de l'image de Speed

        image: Surface scale
            Adaptation de l'image de Speed

        rect: RectType
            Mise d'un rectangle pour les collisions autour de l'image Speed

        rect.x:int
            Génération de la postion de l'image sur l'axe des x de manière aléatoire

        rect.y:int
            Génération de la postion de l'image sur l'axe des y de manière aléatoire
        '''
        super().__init__()

        self.image = pygame.image.load("Images/speed.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(62, 840)
        if self.rect.x in range(340, 535) or self.rect.x == 90 or self.rect.x == 810:
            self.rect.x = random.randint(62, 840)
        self.rect.y = random.randint(110, 680)
        if self.rect.y in range(285, 445) or self.rect.y == 560 or self.rect.y == 60:
            self.rect.y = random.randint(110, 680)

