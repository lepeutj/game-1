import pygame

#creer classe player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		self.velocity=1
		super().__init__()
		self.image=pygame.image.load('assets\player.png')
		self.rect=self.image.get_rect()
		self.rect.x=400
		self.rect.y=500
    