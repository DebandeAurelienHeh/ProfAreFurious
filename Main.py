import pygame
from sys import exit
from Menu import Menu
from Player import Player

'''
Instanciation des différentes classes afin de demarrer le jeu

Boucle de gestion:
    -Game active
    -Gestion des touches
'''
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("Profs are Furious")
clock = pygame.time.Clock()

Width = 1000
Height = 800
screen = pygame.display.set_mode((Width, Height))


player1_car = Player("Car", (pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d))
player2_car = Player("Car", (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT), pos=(800, 400))

player1_tank = Player("Tank", (pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d))
player2_tank = Player("Tank", (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT), pos=(800, 400))

menu = Menu(player1_car, player2_car, player1_tank, player2_tank)
game_active = menu._game_active

keys_pressed = {key: False for key in (pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d, pygame.K_1, pygame.K_2, pygame.K_ESCAPE)}

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        if event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True
            player1_car._vehicle._pressed[event.key] = True
            player2_car._vehicle._pressed[event.key] = True
            player1_tank._vehicle._pressed[event.key] = True
            player2_tank._vehicle._pressed[event.key] = True

        if event.type == pygame.KEYUP:
            player1_car._vehicle._pressed[event.key] = False
            player2_car._vehicle._pressed[event.key] = False
            keys_pressed[event.key] = False
            player2_tank._vehicle._pressed[event.key] = False
            player1_tank._vehicle._pressed[event.key] = False

    if game_active == 1:        # Menu de base
        game_active = menu.starting_screen(screen, keys_pressed)

    if game_active == 2:        # Choix Nombre Joueur
        game_active = menu.player_number(screen, keys_pressed)

    if game_active == 3:        # Choix GameMode Solo
        game_active = menu.gamemode_solo(screen, keys_pressed)

    if game_active == 4:        # Arena Gamemode Solo
        menu.arena_solo(screen, keys_pressed)
        game_active = menu._game_active

    if game_active == 5:        # Survival Gamemode solo
        menu.survival_solo(screen)

    if game_active == 6:        # Choix Gamemode Multiplayer
        menu.gamemode_multiplayer(screen, keys_pressed)
        game_active = menu._game_active

    if game_active == 7:        # Arena Gamemode Multiplayer
        menu.arena_multiplayer(screen, keys_pressed)
        game_active = menu._game_active

    if game_active == 8:        # Pause pour Arena Solo
        menu.pause_solo(screen, keys_pressed)
        game_active = menu.pause_solo(screen, keys_pressed)

    if game_active == 9:        # Pause pour Arena Multiplayer
        menu.pause_multiplayer(screen, keys_pressed)
        game_active = menu.pause_multiplayer(screen, keys_pressed)

    if game_active == 10:       # Game Over
        menu.game_over(screen, keys_pressed)
        game_active = menu._game_active

    pygame.display.update()
    clock.tick(60)
