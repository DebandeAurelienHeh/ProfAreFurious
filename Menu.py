import pygame
import map
import random
import music
from wooden_box import Wooden_box
from power_up import Power_up

'''
Instanciation des différentes classes afin de demarrer le jeu

Boucle de gestion:
    -Game active
    -Gestion des touches
'''

pygame.font.init()

Width = 1000
Height = 800

map = map.Map(Width, Height)
music = music.Music()

random_map = random.randrange(0, len(map.maps))  # Choix aléatoire de la map


text_background = pygame.font.Font("Images/dirtyoldtown.ttf", 100)

# Starting Screen
#background_start = pygame.image.load("Images/VinVoitureFumee.png")
#background_start = pygame.transform.scale(background_start, (1000, 800))

play_text = text_background.render("New Game (1)", False, "aliceblue")
play_text_rect = play_text.get_rect(center=(500, 200))

continue_text = text_background.render("Continue (2)", False, "aliceblue")
continue_text_rect = continue_text.get_rect(center=(500, 400))

quit_text = text_background.render("Quit (esc)", False, "aliceblue")
quit_text_rect = quit_text.get_rect(center=(500, 600))

# Gamemode
#background_gamemode_solo = pygame.image.load("Images/VinDebout.png")
#background_gamemode_solo = pygame.transform.scale(background_gamemode_solo, (1000, 800))

#background_gamemode_multiplayer = pygame.image.load("Images/MultiDezoom.png")
#background_gamemode_multiplayer = pygame.transform.scale(background_gamemode_multiplayer, (1000, 800))

arena_text = text_background.render("Arena (1)", False, "aliceblue")
arena_text_rect = arena_text.get_rect(center=(500, 200))

survival_text = text_background.render("survival soon (2)", False, "aliceblue")
survival_text_rect = survival_text.get_rect(center=(500, 400))

back_text = text_background.render("Back (Esc)", False, "aliceblue")
back_text_rect = back_text.get_rect(center=(500, 600))

# Player_number
#background_player_number = pygame.image.load("Images/VinVoitureFumee.png")
#background_player_number = pygame.transform.scale(background_player_number, (1000, 800))

soloplayer = text_background.render("Soloplayer (1)", False, "aliceblue")
soloplayer_rect = soloplayer.get_rect(center=(500, 200))

multiplayer = text_background.render("Multiplayer (2)", False, "aliceblue")
multiplayer_rect = multiplayer.get_rect(center=(500, 400))

# Pause
pause_text = text_background.render("Pause", False, "aliceblue")
pause_text_rect = pause_text.get_rect(center=(500, 200))

jouer_text = text_background.render("Play (Enter)", False, "aliceblue")
jouer_text_rect = jouer_text.get_rect(center=(500, 400))

Menu_text = text_background.render("Menu (Esc)", False, "aliceblue")
Menu_text_rect = Menu_text.get_rect(center=(500, 600))

# Game Over
game_over_text = text_background.render("Game Over", False, "aliceblue")
game_over_text_rect = game_over_text.get_rect(center=(500, 600))

#game_over_background = pygame.image.load("Images/game_over.png")
#game_over_background = pygame.transform.scale(game_over_background, (1000, 800))


class Menu:
    '''
        Classe servant à l'instanciation de Menu

        Attributs:
        ----------
        game_active: 1
            Demarrage du jeu au stade game active 1

        player1: class
            Utilisation de l'instanciation player 1

        player2: class
            Utilisation de l'instanciation player 2

        player1_tank: class
            Utilisation de l'instanciation player 1 tank

        player2_tank: class
            Utilisation de l'instanciation player 2 tank

        box: class
            Intanciation de la class Wooden_box

        powers: class
            Instanciation de la classe Power_up

        current_music: str
            Musique joué actuellement

        Méthodes:
        ---------
        starting_screen(screen= ecran, key_pressed = [])
            Demarre l'ecran de jeu avec les touches attribué

        gamemode_solo(screen = ecran, key_pressed = [])
            Demarre le mode de jeu seul

        gamemode_multiplayer(screen = ecran, key_pressed = [])
            Demarre le mode de jeu a plusieurs

        player_number(screen = ecran, key_pressed = [])
            Gere le nombre de joueur

        arena_solo(screen = ecran, key_pressed = [])
            Lance le mode arene en solo

        survival_solo(sceeen = ecran)
            Pas implémenter

        arena_multiplayer(screen = ecran, key_pressed = [])
            Lance le mode de jeu arene en multijoueur

        pause_solo(screen = ecran, key_pressed = [])
            Lance le mode pause dans le mode solo

        pause_Multiplayer(screen = ecran, key_pressed = [])
            Lance le mode pause en mode multijoueur

        game_over(screen = ecran, key_pressed = [])
            Lance l'écran de game over

        save_game()
            Pas implémenté

        reset_keys(key_pressed = [])
            Permet de retirer les touches afin de ne plsu les prendre en compte
        '''
    def __init__(self, player1, player2, player1_tank, player2_tank):
        '''
                Construit les attributs necessaire au bon focntionnement

                Paramètres:

                player1: class
                    Utilisation de l'instanciation player 1

                player2: class
                    Utilisation de l'instanciation player 2

                player1_tank: class
                    Utilisation de l'instanciation player 1 tank

                player2_tank: class
                    Utilisation de l'instanciation player 2 tank
                '''
        self._game_active = 1
        self._player1 = player1
        self._player2 = player2
        self._player1_tank = player1_tank
        self._player2_tank = player2_tank
        self._box = Wooden_box()
        self._powers = Power_up()
        self._current_music = ""

    def starting_screen(self, screen, keys_pressed):
        '''
                Demarre l'ecran de jeu avec les touches attribué

                Paramètres:
                screen = ecran
                key_pressed = []

                Return:
                     game_active
                '''
        #screen.blit(background_start, (0, 0))
        screen.fill("black")
        screen.blit(play_text, play_text_rect)
        screen.blit(quit_text, quit_text_rect)
        screen.blit(continue_text, continue_text_rect)
        music.play("menu")
        if keys_pressed.get(pygame.K_1):
            self._game_active = 2
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_ESCAPE):
            exit()
        return self._game_active

    def gamemode_solo(self, screen, keys_pressed):
        '''
                Demarre le mode de jeu seul

                Paramètres:
                    screen = ecran
                    key_pressed = []

                Return:
                     game_active
                '''
        #screen.blit(background_gamemode_solo, (0, 0))
        screen.fill("black")
        screen.blit(arena_text, arena_text_rect)
        screen.blit(survival_text, survival_text_rect)
        screen.blit(back_text, back_text_rect)
        if keys_pressed.get(pygame.K_1):
            self._game_active = 4                                 # Arena Gamemode Solo
            print("fonctionneSolo")
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_2):
            self._game_active = 5                                 # Survival Gamemode solo
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 2                                 # Retour au choix de joueur
            self.reset_keys(keys_pressed)
        return self._game_active

    def gamemode_multiplayer(self, screen, keys_pressed):
        '''
                Demarre le mode de jeu a plusieurs

                Paramètres:
                    screen = ecran
                    key_pressed = []

                Return:
                     game_active
                '''
        #screen.blit(background_gamemode_multiplayer, (0, 0))
        screen.fill("black")
        screen.blit(arena_text, arena_text_rect)
        screen.blit(back_text, back_text_rect)
        if keys_pressed.get(pygame.K_1):
            self._game_active = 7                                 # Arena Gamemode Multiplayer
            print(self._game_active)
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 2                                 # Retour au choix nombre de joueurs
            print(self._game_active)
            self.reset_keys(keys_pressed)
        return self._game_active

    def player_number(self, screen, keys_pressed):
        '''
                Gere le nombre de joueur

                Paramètres:
                    screen = ecran
                    key_pressed = []

                Return:
                     game_active
                '''
        #screen.blit(background_player_number, (0, 0))
        screen.fill("black")
        screen.blit(soloplayer, soloplayer_rect)
        screen.blit(multiplayer, multiplayer_rect)
        screen.blit(back_text, back_text_rect)
        if keys_pressed.get(pygame.K_1):
            self._game_active = 3
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_2):
            self._game_active = 6
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 1
            self.reset_keys(keys_pressed)
        return self._game_active

    def arena_solo(self, screen, keys_pressed):
        '''
                Lance le mode arene en solo

                Paramètres:
                    screen = ecran
                    key_pressed = []

                Return:
                     game_active
        '''
        map.load_map(screen, Width, Height)  # Affichage de la map
        #self._player1.update(screen, map.walls, self._powers.sprite, self._box)
        #self._player1.show(screen)
        self._player1_tank.update(screen, map.walls, self._powers.sprite, self._box)
        self._player1_tank.show(screen)
        map.draw_wall(screen)
        if self._current_music != "game":
            music.stop("menu")
            music.play("game")
            self._current_music = "game"
        screen.blit(self._box.image, self._box.rect)
        self._powers.show(screen)
        Power_up.timer(self._powers)
        if self._powers.duration == 0:  # Chronomètre pour le temps de présence des améliorations
            for sprite in self._powers.sprite:
                for hitboxe in sprite:
                    hitboxe.rect.x = 10000
        if self._powers.delay == 0:  # Temps avant la réaparition des améliorations
            self._powers = Power_up()
        if self._box.is_broken:  # Vérification de collision avec la caisse et la régenère
            self._box = Wooden_box()
            self._box.is_broken = False
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 8
            self.reset_keys(keys_pressed)
            print("pause")
        if self._player1_tank.vehicle.game_over():
            self._game_active = 10
        return self._game_active

    def survival_solo(self, screen):
        '''
               Pas implémenter

               Paramètres:
                   screen = ecran

               Return:
                    NONE
               '''
        pass

    def arena_multiplayer(self, screen, keys_pressed):
        '''
                Lance le mode de jeu arene en multijoueur

                Paramètres:
                    screen = ecran
                    key_pressed = []

                Return:
                     game_active
                '''
        map.load_map(screen, Width, Height)  # Affichage de la map
        """self._player1.update(screen, map.walls, self._powers.sprite, self._box)
        self._player1.show(screen)
        self._player1._vehicle.collide(self._player2._vehicle,screen, map.walls, self._powers.sprite, self._box)
        self._player2.update(screen, map.walls, self._powers.sprite, self._box)
        self._player2.show(screen)
        self._player2._vehicle.collide(self._player1._vehicle,screen , map.walls, self._powers.sprite, self._box)"""
        self._player1_tank.update(screen, map.walls, self._powers.sprite, self._box)
        self._player1_tank.show(screen)
        self._player1_tank._vehicle.collide(self._player2_tank._vehicle, screen, map.walls, self._powers.sprite, self._box)
        self._player2_tank.update(screen, map.walls, self._powers.sprite, self._box)
        self._player2_tank.show(screen)
        self._player2_tank._vehicle.collide(self._player1_tank._vehicle, screen, map.walls, self._powers.sprite, self._box)
        map.draw_wall(screen)
        if self._current_music != "game":
            music.stop("menu")
            music.play("game")
            self._current_music = "game"
        screen.blit(self._box.image, self._box.rect)
        self._powers.show(screen)
        Power_up.timer(self._powers)
        if self._powers.duration == 0:  # Chronomètre pour le temps de présence des améliorations
            for sprite in self._powers.sprite:
                for hitboxe in sprite:
                    hitboxe.rect.x = 10000
        if self._powers.delay == 0:  # Temps avant la réaparition des améliorations
            self._powers = Power_up()
        if self._box.is_broken:  # Vérification de collision avec la caisse et la régenère
            self._box = Wooden_box()
            self._box.is_broken = False
        if self._player1_tank.vehicle.game_over():
            self._game_active = 10
        if self._player2_tank.vehicle.game_over():
            self._game_active = 10
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 9
            self.reset_keys(keys_pressed)
        return self._game_active

    def pause_solo(self, screen, keys_pressed):
        '''
               Lance le mode pause dans le mode solo

               Paramètres:
                   screen = ecran
                   key_pressed = []

               Return:
                    game_active
               '''
        screen.blit(pause_text, pause_text_rect)
        screen.blit(jouer_text, jouer_text_rect)
        screen.blit(Menu_text, Menu_text_rect)
        music.stop("game")
        self._current_music = ""
        if keys_pressed.get(pygame.K_RETURN):
            self._game_active = 4
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 1
            self.reset_keys(keys_pressed)
        return self._game_active

    def pause_multiplayer(self, screen, keys_pressed):
        '''
               Lance le mode pause en mode multijoueur

               Paramètres:
                   screen = ecran
                   key_pressed = []

               Return:
                    game_active
               '''
        screen.blit(pause_text, pause_text_rect)
        screen.blit(jouer_text, jouer_text_rect)
        screen.blit(Menu_text, Menu_text_rect)
        music.stop("game")
        self._current_music = ""
        if keys_pressed.get(pygame.K_RETURN):
            self._game_active = 7
            self.reset_keys(keys_pressed)
        if keys_pressed.get(pygame.K_ESCAPE):
            self._game_active = 1
            self.reset_keys(keys_pressed)
        return self._game_active

    def game_over(self, screen, keys_pressed):
        '''
               Lance l'écran de game over

               Paramètres:
                   screen = ecran
                   key_pressed = []

               Return:
                    NONE
               '''
        #screen.blit(game_over_background, (0, 0))
        screen.fill("black")
        screen.blit(game_over_text, game_over_text_rect)
        if self._current_music != "game_over":
            music.stop("game")
            music.play("game_over")
            self._current_music = "game"
        if keys_pressed.get(pygame.K_ESCAPE):
            exit()

    def save_game(self):
        '''
                Pas implémenté

                Paramètres:

                Return:
                     NONE
                '''
        pass

    def reset_keys(self, keys_pressed):
        '''
                Permet de retirer les touches afin de ne plsu les prendre en compte

                Paramètres:
                    key_pressed = []

                Return:
                     NONE
                '''
        for key in keys_pressed:
            keys_pressed[key] = False

