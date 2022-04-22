import pygame
from player import Player

class Game():
    def __init__(self):
        self.player=Player()
        self.pressed={}


    def move_right(self):
        self.player.rect.x+=self.player.velocity

    def move_left(self):
        self.player.rect.x-=self.player.velocity