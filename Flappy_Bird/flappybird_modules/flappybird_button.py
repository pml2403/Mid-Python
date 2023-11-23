import pygame

class Button():
		def __init__(self, x, y, image, screen):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.topleft = (x, y)
			self.screen = screen

		def draw(self):
			action = False

			#get mouse position
			pos = pygame.mouse.get_pos() #get the position of the mouse

			#check mouseover and clicked conditions
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1:
					action = True

			#draw button
			self.screen.blit(self.image, (self.rect.x, self.rect.y))

			return action