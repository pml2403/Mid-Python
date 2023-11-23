import pygame,sys, random
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("tic-tac-toe")

#define variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

#define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

font = pygame.font.SysFont(None, 40)
again_rect = Rect(screen_width // 2 - 80, screen_height //2, 160, 50)

def draw_grid():
    screen.fill('white')

    for x in range(1,3):
        pygame.draw.line(screen, 'black', (0, x*100), (screen_width, x*100),line_width)
        pygame.draw.line(screen, 'black', (x*100, 0), (x*100,screen_height),line_width)

for x in range(3):
    row = [0]*3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos *100 + 15), (x_pos * 100 + 85, y_pos *100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos *100 + 85), (x_pos * 100 + 85, y_pos *100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red,  (x_pos * 100 + 50, y_pos *100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner
    global game_over
    for x in range(3):
            #check rows
        if markers[x][0] == markers[x][1] == markers[x][2] == 1:
            winner = 1
            game_over = True 
            return game_over
        if markers[x][0] == markers[x][1] == markers[x][2] == -1:
            winner = 2
            game_over = True
            return game_over
        #check columns
        if markers[0][x] == markers[1][x] == markers[2][x] == 1:
            winner = 1
            game_over = True
            return game_over
        if markers[0][x] == markers[1][x] == markers[2][x] == -1:
            winner = 2
            game_over = True
            return game_over
    #check cross
    if markers[0][0] == markers[1][1] == markers[2][2] == 1 or markers[0][2] == markers[1][1] == markers[2][0] == 1:
        winner = 1
        game_over = True
        return game_over
    if markers[0][0] == markers[1][1] == markers[2][2] == -1 or markers[0][2] == markers[1][1] == markers[2][0] == -1:
        winner = 2
        game_over = True
        return game_over
    #check tie
    if markers[0][1] != 0 and markers[0][2] != 0 and markers[0][0] != 0 and markers[1][1] != 0 and markers[1][2] != 0 and markers[1][0] != 0 and markers[2][1] != 0 and markers[2][2] != 0 and markers[2][0] != 0  :
        game_over = True
        return game_over

def draw_winner(winner):
    if winner != 0:
        win_text = "Player " + str(winner) + " wins!"
        win_img = font.render(win_text, True, blue)
        pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
        screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))
        again_text = "Play Again?"
        again_img = font.render(again_text, True, blue)
        pygame.draw.rect(screen, green, again_rect)
        screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 +10))
    # tie
    else:
        tie_text= "Tie!"
        tie_img = font.render(tie_text, True, blue)
        pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
        screen.blit(tie_img, (screen_width // 2 - 100, screen_height // 2 - 50))
        again_text = "Play Again?"
        again_img = font.render(again_text, True, blue)
        pygame.draw.rect(screen, green, again_rect)
        screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 +10))

while True:
    
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked=True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked=False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        draw_winner(winner)  
        #check for mouseclick to see if user has clicked on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked=True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked=False    
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset variable
                markers=[]
                pos=[]
                player=1
                winner=0
                game_over = False
                for x in range(3):
                    row= [0]*3
                    markers.append(row)
    pygame.display.update()

