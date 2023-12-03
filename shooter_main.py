import pygame 
import os
import random
from shooter_modules.settings import *
import shooter_modules.game as game

pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock() #control the frame rate in 1 second

run = True
while run:
    PLAY.blit(BACKGROUND, (0,0))
    title = title_font.render('PLAY', 1, (255,255,255))
    PLAY.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.game()
    
    pygame.display.update()