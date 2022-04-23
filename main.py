import pygame
from game import Game
pygame.init()


# générer fenêtre jeu
pygame.display.set_caption("comet fall Game")
screen=pygame.display.set_mode((1080, 720))

#importer arriere plan du jeu
background= pygame.image.load('assets/bg.jpg')

game= Game()
running=True

#boucle tant que cette condition est vrai
while running:
	# appliquer arriere plan du jeu
	screen.blit(background,(0,-200))

	#appliquer l'image du joueur
	screen.blit(game.player.image, game.player.rect)

	#récupérer les projectiles 
	for projectile in game.player.all_projectiles:
		projectile.move()

	#récupérer monstres
	for monster in game.all_monsters:
		monster.forward()

	#appliquer images projectiles
	game.player.all_projectiles.draw(screen)

	# appliquer images monstres
	game.all_monsters.draw(screen)

	# appliquer l'image de l'enemy 
	screen.blit(game.enemy.image, game.enemy.rect)

	#mettre a jour l'ecran
	pygame.display.flip()

	# verif si le joueur veut aller à gauche ou à droite
	if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width<=screen.get_width():
		game.move_right()
	
	elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>=0:
		game.move_left()

	#si joueur ferme la fenêtre
	for event in pygame.event.get():
		# l'évenement est fermeture
		if event.type==pygame.QUIT:
			running=False
			pygame.quit()

		# détecter si un joueur lache la touche du clavier
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key]=True
		
			# touche space appuyée
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()

		elif event.type == pygame.KEYUP:
			game.pressed[event.key]=False