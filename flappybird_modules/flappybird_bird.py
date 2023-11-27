import pygame

class Bird(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.images = []
			self.index = 0
			self.counter = 0 #control the speed

			bird1 = pygame.image.load("flappybird_images/bird1.png").convert_alpha()
			bird2 = pygame.image.load("flappybird_images/bird2.png").convert_alpha()
			bird3 = pygame.image.load("flappybird_images/bird3.png").convert_alpha()
			self.images.append(bird1)
			self.images.append(bird2)
			self.images.append(bird3)

			self.image = self.images[self.index]
			self.rect = self.image.get_rect()
			self.rect.center = [x, y]
			self.vel = 0
			self.clicked = False

		def update(self, flying, game_over, flap_sound):
			if flying == True:
				#apply gravity
				self.vel += 0.5
				if self.vel > 8:
					self.vel = 8
				if self.rect.bottom < 550:
					self.rect.y += self.vel

			if game_over == False:
				#jump
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: 
					self.clicked = True
					self.vel = -10
					flap_sound.play()
				if pygame.mouse.get_pressed()[0] == 0:
					self.clicked = False

				#handle the animation
				flap_cooldown = 5
				self.counter += 1
				
				if self.counter > flap_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >= len(self.images):
						self.index = 0

				#rotate the bird
				self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
			else:
				#point the bird at the ground
				self.image = pygame.transform.rotate(self.images[self.index], -90)