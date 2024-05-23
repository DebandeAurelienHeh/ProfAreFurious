import pygame

from heal import Heal
from push import Push
from speed import Speed


class Power_up:
    '''
    Class pour instancier les différents power_up sous forme de groupe

    ...

    Attributs:
    ---------

    duration:int
        Durée d'apparition des power-up sur la carte

    delay:int
        Temps avant la réaparition des power-up

    push:Class
        Instanciation de la classe Push

    sprite_push: Group.sprite
        Création de groupe de sprite pour le power-up push

    sprite_push.add
        Ajout du sprite push dans le group sprite_ush

    speed: Class
        Instanciation de la classe Push

    sprite_speed: Group.sprite
        Création de groupe de sprite pour le power-up speed

    sprite_speed.add
        Ajout du sprite push dans le group sprite_push

    speed: Class
        Instanciation de la classe Push

    sprite_speed: Group.sprite
        Création de groupe de sprite pour le power-up speed

    sprite_speed.add
        Ajout du sprite push dans le group sprite_speed

    heal: Class
        Instanciation de la classe Push

    sprite_heal: Group.sprite
        Création de groupe de sprite pour le power-up heal

    sprite_heal.add
        Ajout du sprite push dans le group sprite_heal

    sprite: Liste
        Liste contenant les groupes de sprite des power-up


    Méthodes:
    --------

    show(screen = écran)
        Permet l'affichage des sprites des power-up

    timer()
        Permet la gestion des cycles de d'apparition et de réaparition
    '''

    def __init__(self):
        '''
            Construit tous les attributs nécessaire au fonctionnement

            duration:int
                Durée d'apparition des power-up sur la carte

            delay:int
                Temps avant la réaparition des power-up

            push:Class
                Instanciation de la classe Push

            sprite_push: Group.sprite
                Création de groupe de sprite pour le power-up push

            sprite_push.add
                Ajout du sprite push dans le group sprite_ush

            speed: Class
                Instanciation de la classe Push

            sprite_speed: Group.sprite
                Création de groupe de sprite pour le power-up speed

            sprite_speed.add
                Ajout du sprite push dans le group sprite_push

            speed: Class
                Instanciation de la classe Push

            sprite_speed: Group.sprite
                Création de groupe de sprite pour le power-up speed

            sprite_speed.add
                Ajout du sprite push dans le group sprite_speed

            heal: Class
                Instanciation de la classe Push

            sprite_heal: Group.sprite
                Création de groupe de sprite pour le power-up heal

            sprite_heal.add
                Ajout du sprite push dans le group sprite_heal

            sprite: Liste
                Liste contenant les groupes de sprite des power-up
        '''
        self.duration = 600
        self.delay = 600
        self.push = Push()
        self.sprite_push = pygame.sprite.Group()
        self.sprite_push.add(self.push)
        self.speed = Speed()
        self.sprite_speed = pygame.sprite.Group()
        self.sprite_speed.add(self.speed)
        self.heal = Heal()
        self.sprite_heal = pygame.sprite.Group()
        self.sprite_heal.add(self.heal)
        self.sprite = [
            self.sprite_push,
            self.sprite_speed,
            self.sprite_heal
        ]




    def show(self,screen):
        '''
        Permet l'affichage des sprites

        Paramètre:

        screen :écran

        Return:
            NONE
        '''
        screen.blit(self.push.image,self.push.rect)
        screen.blit(self.speed.image, self.speed.rect)
        screen.blit(self.heal.image, self.heal.rect)

    def timer(self):
        '''
        Chronomètre pour les cycles d'apparition et de réaparition

        Paramètre:
        NONE

        Return:
            NONE
        '''
        if self.duration == 0:
            if self.delay == 0:
                self.duration = 10
                self.delay = 10
            else:
                self.delay -= 1
        else:
            self.duration -= 1








