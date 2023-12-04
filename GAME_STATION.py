from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk

window = CTk()
window.geometry('500x650')
window.title('GAME STATION')
set_appearance_mode('dark')

background_image = Image.open('game_station_assets/background.jpg')
background_image_tk = ImageTk.PhotoImage(background_image)
background = CTkLabel(window, 
                    image = background_image_tk)
background.place(relwidth = 1, relheight = 1)

title_image = Image.open('game_station_assets/game_station_text.png').resize((500, 150))
title_image_tk = ImageTk.PhotoImage(title_image)
title = CTkButton(window, 
                image = title_image_tk,
                fg_color = 'transparent',
                bg_color = 'transparent',
                text = '',
                border_color = 'blue',
                border_width = 2,
                corner_radius = 10,
                state = DISABLED)
title.place(relx = 0.5, rely = 0.17,anchor='center')

game_frame = CTkFrame(window, fg_color = '#3b3b3d', border_width = 0)
game_frame.place(relx = 0.5, rely = 0.65, relwidth = 0.8, relheight = 0.5, anchor = CENTER)

def import_flappy():
    import flappybird_main

def import_snake():
    import snake_main
        
def import_shooter():
    import shooter_main

def import_tictactoe():
    import tictactoe_main

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
                        text = 'Snake', 
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
                        text = 'Shooter', 
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

window.mainloop()