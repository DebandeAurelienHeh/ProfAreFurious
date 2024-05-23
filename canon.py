import pygame
from obstacle import Obstacle

class Canon(Obstacle):

    def __init__(self,pos_x,pos_y,min_pos_y=0,max_pos_y=0,direction = 1):
        super().__init__()
        self.image = pygame.image.load("cannon.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 40))
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.min_pos_y = min_pos_y
        self.max_pos_y = max_pos_y
        self.direction = direction
        self.all_balls = pygame.sprite.Group()
        self.percent = 0

    def add_percent(self):
        self.percent += 1

    def shoot(self):
        self.all_balls.add(Projectile_canon())


    def move(self):
        if self.rect.y == self.min_pos_y:
            self.direction = 1
        elif self.rect.y == self.max_pos_y:
            self.direction = 2
        if self.direction == 1:
            self.rect.y += 1
        else:
            self.rect.y -= 1