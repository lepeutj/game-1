from typing_extensions import Self
import pygame
from projectile import Projectile
#creer classe player

class Player(pygame.sprite.Sprite):
	def __init__(self):
        super().__init__()
		self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
		self.rect.x = 400
		self.rect.y = 500
		self.image = pygame.image.load('assets\player.png')
		self.rect = self.image.get_rect()