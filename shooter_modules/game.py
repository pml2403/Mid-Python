import pygame
from shooter_modules.settings import *

pygame.init()

def draw_winner(text):
    win_text = WINNER_FONT.render(text, 1, WHITE)
    PLAY.blit(win_text, (WIDTH/2 - win_text.get_width()/2, HEIGHT/2 - win_text.get_height()/2)) #middle of screen
    pygame.display.update()
    pygame.time.delay(1000)

def handle_bullet(green_bullets, blue_bullets, green, blue):
    for bullets in green_bullets:
        bullets.x += BULLET_VEL
        if blue.colliderect(bullets):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            green_bullets.remove(bullets)
        elif bullets.x > WIDTH:
            green_bullets.remove(bullets)
    
    for bullets in blue_bullets:
        bullets.x -= BULLET_VEL
        if green.colliderect(bullets):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            blue_bullets.remove(bullets)
        elif bullets.x < 0:
            blue_bullets.remove(bullets)

def draw_background(green, blue, green_bullets, blue_bullets, green_health, blue_health):
    PLAY.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(PLAY, BLACK, BORDER)
    green_health_text = HEALTH_FONT.render("Health: " + str(green_health), 1, WHITE)
    blue_health_text = HEALTH_FONT.render("Health: " + str(blue_health), 1, WHITE)
    PLAY.blit(blue_health_text, (WIDTH - blue_health_text.get_width() - 10, 10)) #top right of screen + 10 pixels down
    PLAY.blit(green_health_text, (10, 10))
    PLAY.blit(GREEN_SPACESHIP, (green.x, green.y))
    PLAY.blit(BLUE_SPACESHIP, (blue.x, blue.y))

    for bullet in green_bullets:
        if pygame.key.get_pressed()[pygame.K_LCTRL]:
            pygame.draw.rect(PLAY, GREEN, bullet)
        else:
            pygame.draw.rect(PLAY, RED, bullet)

    for bullet in blue_bullets:
        if pygame.key.get_pressed()[pygame.K_RCTRL]:
            pygame.draw.rect(PLAY, BLUE, bullet)
        else:
            pygame.draw.rect(PLAY, YELLOW, bullet)

    pygame.display.update()

def green_move(key_pressed, green):
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a] and green.x - VEL > 0: #left and don't move out of screen
        green.x -= VEL
    if key_pressed[pygame.K_d] and green.x + VEL + green.width < BORDER.x: #right and dont move out of screen
        green.x += VEL
    if key_pressed[pygame.K_w] and green.y - VEL > 0: #up
        green.y -= VEL
    if key_pressed[pygame.K_s] and green.y + VEL + green.height < HEIGHT - 20: #down
        green.y += VEL

def blue_move(key_pressed, blue):
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT] and blue.x - VEL > BORDER.x + BORDER.width: #left
        blue.x -= VEL
    if key_pressed[pygame.K_RIGHT] and blue.x + VEL + blue.width < WIDTH: #right
        blue.x += VEL
    if key_pressed[pygame.K_UP] and blue.y - VEL > 0: #up
        blue.y -= VEL
    if key_pressed[pygame.K_DOWN] and blue.y + VEL + blue.height < HEIGHT - 20: #down
        blue.y += VEL

def game():
    green = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    blue =  pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    green_bullets = []
    blue_bullets = []

    green_health = 100
    blue_health = 100

    space_press_count = 0

    clock = pygame.time.Clock() #control the frame rate in 1 second
    run = True
    BACKGROUND_SOUND.play()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_press_count += 1

                if space_press_count % 2 == 1:  # Check if space key was pressed an odd number of times
                    if BACKGROUND_SOUND.get_volume():
                        BACKGROUND_SOUND.stop()
                elif space_press_count % 2 == 0:
                    BACKGROUND_SOUND.play()

            if event.type == pygame.KEYDOWN:
                # Calculate the middle of the spaceship's image
                if event.key == pygame.K_LALT and len(green_bullets) < MAX_BULLETS:
                    bullet_x = green.x + (green.width + 20) / 2
                    bullet_y = green.y + (green.height + 20) / 2

                    # Create a new bullet at the middle of the spaceship
                    bullet = pygame.Rect(bullet_x, bullet_y, 10, 5) #do day va dai cua dan

                    # Add the bullet to the green bullets list
                    green_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RALT and len(blue_bullets) < MAX_BULLETS:
                    # Calculate the middle of the spaceship's image
                    bullet_x = (blue.x) + (blue.width + 20) / 2
                    bullet_y = (blue.y) + (blue.height + 20) / 2

                    # Create a new bullet at the middle of the spaceship
                    bullet = pygame.Rect(bullet_x, bullet_y, 10, 5)

                    # Add the bullet to the blue bullets list
                    blue_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        
            if event.type == BLUE_HIT:
                green_health -= 5
                BULLET_HIT_SOUND.play()
                
            if event.type == GREEN_HIT:
                blue_health -= 5
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if blue_health == 0:
            winner_text = "PLAYER2 WINS!"
        if green_health == 0:
            winner_text = "PLAYER1 WINS!"
        if winner_text != "":
            draw_winner(winner_text)
            while True:
                title = title_font.render('PLAY', 1, (255,255,255))
                PLAY.blit(BACKGROUND, (0,0))
                PLAY.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        space_press_count += 1

                        if space_press_count % 2 == 1:  # Check if space key was pressed an odd number of times
                            if BACKGROUND_SOUND.get_volume():
                                BACKGROUND_SOUND.stop()
                        elif space_press_count % 2 == 0:
                            BACKGROUND_SOUND.play()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        BACKGROUND_SOUND.stop()

        handle_bullet(green_bullets, blue_bullets, green, blue)
        press = pygame.key.get_pressed()
        draw_background(green, blue, green_bullets, blue_bullets, blue_health, green_health)
        green_move(press, green)
        blue_move(press, blue)

        



