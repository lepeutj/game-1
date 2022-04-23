import pygame
from PIL import Image
enemy_image=Image.open("assets/projectile.png")
enemy_image.resize((50,50))
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		self.velocity=1
		super().__init__()
		self.image=pygame.image.load('assets/comet.png')

		self.rect=self.image.get_rect()
		self.rect.x=200
		self.rect.y=200