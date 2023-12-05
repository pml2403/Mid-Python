import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1280, 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 80, 50
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.Font('shooter_assets\ARCADE.TTF', 50)
WINNER_FONT = pygame.font.Font('shooter_assets\ARCADECLASSIC.TTF', 150)
title_font = pygame.font.Font("shooter_assets\ARCADECLASSIC.TTF", 200)

BULLET_HIT_SOUND = pygame.mixer.Sound('shooter_assets\Assets_Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('shooter_assets\Gun+Silencer.mp3')
BACKGROUND_SOUND = pygame.mixer.Sound('shooter_assets\Wallpaper(chosic.com).mp3')

BULLET_VEL = 7
MAX_BULLETS = 10

GREEN_HIT = pygame.USEREVENT + 1
BLUE_HIT = pygame.USEREVENT + 2

PLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GALAXY SHOOTER")

GREEN_SPACESHIP = pygame.image.load(os.path.join('shooter_assets', 'green spaceship.png'))
GREEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(GREEN_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BLUE_SPACESHIP = pygame.image.load(os.path.join('shooter_assets', 'blue spaceship.png'))
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(BLUE_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

BACKGROUND = pygame.image.load(os.path.join('shooter_assets', 'background.jpg'))