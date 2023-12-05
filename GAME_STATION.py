from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk

window = CTk()
window.geometry('500x650')
window.title('GAME STATION')
set_appearance_mode('dark')

#import games
def import_flappy():
    import flappybird_main

def import_snake():
    import snake_main
        
def import_shooter():
    import shooter_main

def import_tictactoe():
    import tictactoe_main

background_image = Image.open('game_station_assets/background.jpg')
background_image_tk = ImageTk.PhotoImage(background_image)
background = CTkLabel(window, 
                    image = background_image_tk)
background.place(relwidth = 1, relheight = 1)

title_image = Image.open('game_station_assets/game_station_text.png').resize((500, 150))
title_image_tk = ImageTk.PhotoImage(title_image)
title = CTkButton(window, 
                image = title_image_tk,
                fg_color = '#1A0950',
                bg_color = '#1A0950',
                text = '',
                border_color = 'blue',
                border_width = 2,
                corner_radius = 10,
                state = DISABLED)
title.place(relx = 0.5, rely = 0.17,anchor='center')

game_frame = CTkFrame(window, fg_color = '#401E81', border_width = 0)
game_frame.place(relx = 0.5, rely = 0.65, relwidth = 0.8, relheight = 0.5, anchor = CENTER)

flappy_logo = Image.open("game_station_assets/flappybird_logo.png").resize((100, 100))
flappy_logo_tk = ImageTk.PhotoImage(flappy_logo)

flappy_button = CTkButton(game_frame, 
                        text = 'Flappy Bird', 
                        font = ('Roboto', 20, 'bold'),
                        fg_color = 'transparent',                          
                        image = flappy_logo_tk,
                        text_color = '#e8eded',
                        compound = TOP,
                        command = import_flappy)
flappy_button.place(relx = 0.25, rely = 0.25, anchor = CENTER)

snake_logo = Image.open("game_station_assets/snake_logo.png").resize((100, 100))
snake_logo_tk = ImageTk.PhotoImage(snake_logo)

snake_button = CTkButton(game_frame, 
                        text = 'Snake Game', 
                        font = ('Roboto', 20, 'bold'),
                        fg_color = 'transparent',
                        text_color = '#e8eded',
                        image = snake_logo_tk,
                        compound = TOP,
                        command = import_snake)
snake_button.place(relx = 0.75, rely = 0.25, anchor = CENTER)

shooter_logo = Image.open("game_station_assets/shooter_logo.png").resize((100, 100))
shooter_logo_tk = ImageTk.PhotoImage(shooter_logo)

shooter_button = CTkButton(game_frame, 
                        text = 'Space Shooter', 
                        font = ('Roboto', 20, 'bold'),
                        fg_color = 'transparent',
                        text_color = '#e8eded',
                        image = shooter_logo_tk,
                        compound = TOP,
                        command = import_shooter)
shooter_button.place(relx = 0.25, rely = 0.75, anchor = CENTER)

tictactoe_logo = Image.open("game_station_assets/tictactoe_logo.png").resize((100, 100))
tictactoe_logo_tk = ImageTk.PhotoImage(tictactoe_logo)

tictactoe_button = CTkButton(game_frame, 
                            text = 'Tic-Tac-Toe', 
                            font = ('Roboto', 20, 'bold'),
                            fg_color = 'transparent',
                            text_color = '#e8eded',
                            image = tictactoe_logo_tk,
                            compound = TOP,
                            command = import_tictactoe)
tictactoe_button.place(relx = 0.75, rely = 0.75, anchor = CENTER)

def rules_appear():
    if rules_frame.winfo_y() > 650:
        rules_frame.place(relx = 0.5, rely = 0.42, anchor = CENTER)
    else:
        rules_frame.place(relx = 0.5, rely = 1.5)
    
game_rules = CTkButton(window, 
                       text = 'How to play',
                       font = ('Roboto', 15),
                       border_color = '#f50ae9',
                       border_width = 1,
                       fg_color = '#1A0950',
                       hover_color = '#410385',
                       command = rules_appear,
                       width = 200)
game_rules.place(relx = 0.5, rely = 0.32, anchor = CENTER)

rules_frame = CTkFrame(window, 
                       fg_color = 'transparent',
                       bg_color = 'transparent',
                       width = 200,
                       height = 100)
rules_frame.place(relx = 0.5, rely = 1.5)
rule_flappy = CTkButton(rules_frame,
                        fg_color = '#1A0950',
                        corner_radius = 0,
                        text = 'Flappy Bird',
                        hover_color = '#35036b')
rule_flappy.bind('<Button-1>', lambda event: image_appear(1))
rule_flappy.place(relx = 0.5, rely = 0.25, relwidth = 1, relheight = 0.25, anchor = S)
rule_snake = CTkButton(rules_frame,  
                       fg_color = '#1A0950',
                       corner_radius = 0,
                       text = 'Snake Game',
                       hover_color = '#35036b')
rule_snake.bind('<Button-1>', lambda event: image_appear(2))
rule_snake.place(relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.25, anchor = S)
rule_shooter = CTkButton(rules_frame, 
                         fg_color = '#1A0950',
                         corner_radius = 0,
                         text = 'Space Shooter',
                         hover_color = '#35036b')
rule_shooter.bind('<Button-1>', lambda event: image_appear(3))
rule_shooter.place(relx = 0.5, rely = 0.75, relwidth = 1, relheight = 0.25, anchor = S)
rule_tic = CTkButton(rules_frame,  
                     fg_color = '#1A0950',
                     corner_radius = 0,
                     text = 'Tic-Tac-Toe',
                     hover_color = '#35036b')
rule_tic.bind('<Button-1>', lambda event: image_appear(4))
rule_tic.place(relx = 0.5, rely = 1, relwidth = 1, relheight = 0.25, anchor = S)

def close_rule_window():
    image_frame.place(rely = 1.5)
    close_button.place(rely = 1.5)

image_frame = CTkFrame(window, 
                       fg_color = 'black', 
                       width = 300, 
                       height = 400)
close_button = CTkButton(image_frame,
                         fg_color = 'red',
                         text = 'X',
                         text_color = 'white',
                         font = ('Roboto', 10, 'bold'),
                         corner_radius = 0,
                         width = 24,
                         height = 24,
                         command = close_rule_window)

def image_appear(number):
    global image_frame
    rule_image = Image.open(f"game_station_assets/Rule_{number}.png").resize((460, 600))
    rule_image_tk = ImageTk.PhotoImage(rule_image)
    rule_label = CTkLabel(image_frame, 
                          image = rule_image_tk,
                          text = '',
                          corner_radius = 0)
    rule_label.place(relx = 0.5, rely = 0.525, relwidth = 1, relheight = 0.95, anchor = CENTER)
    
    image_frame.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    close_button.place(relx = 1, rely = 0, anchor = NE)

window.mainloop()