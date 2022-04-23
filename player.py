from matplotlib.pyplot import cla
import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity=1
        self.all_projectiles=pygame.sprite.Group()
        self.image=pygame.image.load('assets/player.png')
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=500
       
    
    def launch_projectile(self):
        #Créer projectile
        self.all_projectiles.add(Projectile(self))
    
    

    
