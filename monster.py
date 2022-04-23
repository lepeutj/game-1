import pygame

# définir la classe monster
class Monster(pygame.sprite.Sprite):
    def __init__(self, game): 
        self.game=game
        super().__init__()
        self.velocity = 0.001
        self.image=pygame.image.load('assets/mummy.png')
        self.rect=self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    def forward(self):
        # vérifier collision avec joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        
    