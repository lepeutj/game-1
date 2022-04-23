import imp
import pygame
from player import Player
from enemy import Enemy 
from projectile import Projectile
from monster import Monster

class Game():
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.enemy = Enemy()
        self.pressed = {}
        self.spawn_monster()



    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.check_collision(self.player, self.all_monsters): 
            self.player.rect.x += self.player.velocity

    def move_left(self):
        self.player.rect.x -= self.player.velocity

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)