import pygame
import random


class Map:
    def __init__(self, width, height):
        # SREEN AND MAP
        self.width = width
        self.height = height
        self.maps = ["images/maps/map1.jpg", "images/maps/map2.jpg", "images/maps/map3.jpg"]
        self.random_map = random.randint(0, len(self.maps) -1)
        # WALLS
        self.wall_width = 50
        self.wall_height = 50
        self.wall_posx = [i for i in range(100, 900, 50)]
        self.wall_posy = [i for i in range(100, 700, 50)]
        self.wall_image = pygame.image.load("images/obstacle/wall.png")
        self.wall_image = pygame.transform.scale(self.wall_image, (self.wall_width, self.wall_height))
        self.maps_images = [pygame.image.load(map_path) for map_path in self.maps]

    def load_map(self, screen, width, height):
        loaded_map = self.maps_images[self.random_map]
        map_scale = pygame.transform.scale(loaded_map, (width, height))
        screen.blit(map_scale, (0, 0))
        if not hasattr(self, 'walls'):
            self.walls = [self.wall(screen, 130, 600),
                          self.wall(screen, 500, 100),
                          self.wall(screen, 450, 460),
                          self.wall(screen, 850, 390)]

    def wall(self, screen, x, y):
        wall = self.wall_image
        wall = pygame.transform.scale(wall, (self.wall_width, self.wall_height))
        screen.blit(wall, (x, y))
        wall_rect = wall.get_rect()
        wall_rect.topleft = (x, y)
        return wall_rect

    def draw_wall(self, screen):
        for wall in self.walls:
            screen.blit(self.wall_image, wall)
