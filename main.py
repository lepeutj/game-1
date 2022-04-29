import pygame
from game import Game
import numpy as np
import random
from pynput.keyboard import Key, Controller

pygame.init()
keyboard = Controller()

# générer fenêtre jeu
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# importer ecran d'acceuil
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()/4

# importer bouton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width()/3-25
play_button_rect.y = screen.get_height()/2+40
action = []

def right():
    keyboard.release(Key.left)
    keyboard.press(Key.right)




def left():
    keyboard.release(Key.right)
    keyboard.press(Key.left)



def move():
    if random.randint (0,1) == 0:
        right()
        action = 1
    else:
        left()
        action = 0

    return action



def get_data(game):

    X = []
    Y = []

    X = game.player.rect.x

    enemy_list = game.all_enemy.sprites()

    for i in range(0,3):
        if (len(enemy_list) == 3):
            Y = np.append(Y,[enemy_list[i].rect.x,enemy_list[i].rect.y,enemy_list[i].velocity])

    X = np.append(X,Y)

    return X







# Charger le jeu
game = Game()
running = True

# boucle tant que cette condition est vrai
while running:
    # appliquer arriere plan du jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencé
    if game.is_playing:

    # déclencher les instructions de la partie
        print(get_data(game), move(),game.score)
        game.update(screen)



    else:
        # ecran de bienvenue
        screen.blit(banner, banner_rect)
        font = pygame.font.SysFont('monospace', 16)
        score_text = font.render(f'Score : {game.previous_score}', 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        # bouton play
        screen.blit(play_button, play_button_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si joueur ferme la fenêtre
    for event in pygame.event.get():


        # l'évenement est fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # détecter si un joueur lache la touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification pour savoir si la souris est en collision avec le bouton joueur
            if play_button_rect.collidepoint(event.pos):
                # jeux en mode lancé
                game.start()
