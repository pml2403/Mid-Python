import pygame 
from shooter_modules.settings import *
import shooter_modules.game as game

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock() #control the frame rate in 1 second

running = True

while running:
    # Draw background and title
    PLAY.blit(BACKGROUND, (0, 0))
    title = title_font.render('PLAY', 1, (255, 255, 255))
    PLAY.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))

    # Update the display
    pygame.display.update()

  # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
        # Start the game when clicking on the play area
            game.game()