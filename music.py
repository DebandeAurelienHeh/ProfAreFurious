import pygame

class Music:
    '''
    Classe servant à l'instanciation de Music

    Attributs:
    ---------

    music: List
        Liste contenant les différentes musiques

    menu: music
        Musique joué dans le menu

    game: music
        Musique joué durant la partie

    game_over: music
        Musique joué lors ud game_over

    Méthodes:
    --------

    Play(music = musique qui doit être joué)
        Permet de lancer la musique

    Stop(music = musique qui doit être joué)
        Permet de stopper la musique


    '''
    def __init__(self):
        '''
        Construit tous les attributs nécessaire au fonctionnement

        music: List
            Liste contenant les différentes musiques

        menu: music
            Musique joué dans le menu

        game: music
            Musique joué durant la partie

        game_over: music
            Musique joué lors ud game_over
        '''
        pygame.mixer.init()
        self.music = ["music/menu.mp3", "music/game.mp3", "music/game_over.mp3"]
        self.menu = pygame.mixer.Sound(self.music[0])
        self.game = pygame.mixer.Sound(self.music[1])
        self.game_over = pygame.mixer.Sound(self.music[2])

    def play(self, music):
        '''
        Permet de lancer la musique correspondante

        Paramètre:
            music: la musique qui est joué
        Return:
             NONE
        '''
        try:
            if music == "menu":
                self.menu.play()
                return self.menu
            elif music == "game":
                self.game.play()
                return self.game
            elif music == "game_over":
                self.game_over.play()
                return self.game_over
        except: 
            print("Error loading music")
        
    def stop(self, music):
        '''
        Permet d'arreter la musique

        Paramètre:
            music: la musique qui est joué
        Return:
            NONE
        '''
        pygame.mixer.Sound.stop(self.play(music))


print(Music.__doc__)



