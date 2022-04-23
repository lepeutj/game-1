import pygame
#Définir les projectiles
class Projectile(pygame.sprite.Sprite):

    # def constructeur
    def __init__(self, player):
        super().__init__()
        self.player=player
        self.velocity=2
        self.image=pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect=self.image.get_rect()
        self.rect.x = player.rect.x+22
        self.rect.y = player.rect.y+100
        self.origin_image=self.image
        self.angle=0

    def rotate(self):
        #tourner le projectile
        self.angle +=1
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)

    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # vérifier si projectile entre en collision avec monster
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            #suprimer projectile
            self.remove()


        
        #verifier si projectile n'est plus visible
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()