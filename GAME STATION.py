from customtkinter import *
from random import choice
import tkinter
import importlib

window = CTk()
window.geometry('500x600')
window.title('GAME STATION')
set_appearance_mode('dark')

names = ['mailinh@gmail.com', 'baophung@gmail.com', 'leduy@gmail.com', 'lethao@gmail.com'] 
passwords = ['123456', '223456', '322456', '422456']

button_x = 0.5
game_frame_x = 1.5

flappybird_main = 'flappybird_main'
snake_main = 'snake_main'
shooter_main = 'shooter_main'
tictactoe_main = 'tictactoe_main'

#functions
def temp_text_delete(thing):
    thing.delete(0, END)
    thing.configure(text_color = ('black', 'white'))
    if thing == password:
        password.configure(show = '*')

def check_name(event):
    if '@gmail.com' not in email.get():
        respond_email.configure(text = 'Invalid syntax! Please check again', 
                                text_color = 'red')
    else:
        if email.get() in names:
            respond_email.configure(text = 'Email exist', 
                                    text_color = 'green')
            password.focus_set()
        else:
            respond_email.configure(text = "Account doesn't exist. Please try again", 
                                    text_color = 'red')

def check_password():
    account_index = names.index(email.get())
    if password.get() != passwords[account_index]:
        respond_password.configure(text = 'Wrong password. Please check if there is a mistake with the password, or the email name', 
                                   text_color = 'red')
    else:
        respond_password.configure(text = 'Logged in successfully', 
                                   text_color = 'green')
        window.after(900, turn_to_game_page)

def turn_to_game_page():
    global button_x
    button_x -= 0.03
    login_frame.place(relx = button_x, rely = 0.6, anchor = CENTER)

    if button_x > -1.2:
        window.after(10, turn_to_game_page)
    else:
        move_game_frame()

def move_game_frame():
    global game_frame_x
    game_frame_x -= 0.03
    game_frame.place(relx = game_frame_x, rely = 0.65, relwidth = 0.8, relheight = 0.5, anchor = CENTER)

    if game_frame_x > 0.5:
        window.after(10, move_game_frame)
    else:
        game_frame.place(relx = 0.5, rely = 0.65, relwidth = 0.8, relheight = 0.5, anchor = CENTER)

def import_flappy():
    import flappybird_main

def import_snake():
    import snake_main

def import_shooter():
    import shooter_main

def import_tictactoe():
    import tictactoe_main

def sign_up():
    pass

title = CTkLabel(window, text = 'GAME STATION', 
                 font = ('Arial', 60, 'bold'), 
                 text_color = '#023ebf')
title.place(relx = 0.5, rely = 0.2, anchor='center')

login_frame = CTkFrame(window, width = 450, height = 300, fg_color = ('#0a0838', '#3b3b3d'))
login_frame.place(relx = 0.5, rely = 0.6, anchor = CENTER)

login_frame_text = CTkLabel(login_frame, text = 'Log in to your account to start playing', 
                            font = ('Roboto', 18))
login_frame_text.place(relx = 0.5, rely = 0.13, anchor = CENTER)

email = CTkEntry(login_frame, 
                 font = ('Roboto', 15), 
                 width = 380, 
                 text_color = '#acafb5')
email.place(relx = 0.5, rely = 0.3, anchor = CENTER)
email.insert(0, 'Enter your email...')
email.bind('<FocusIn>', lambda event: temp_text_delete(email))
email.bind('<Return>', check_name)

respond_email = CTkLabel(login_frame, 
                         bg_color='transparent', 
                         text = '', 
                         font = ('Roboto', 12), 
                         height = 20, 
                         compound = LEFT)
respond_email.place(relx = 0.08, rely = 0.39, anchor = W)

password = CTkEntry(login_frame, 
                    font = ('Roboto', 15), 
                    width = 380, text_color = '#acafb5')
password.place(relx = 0.5, rely = 0.48, anchor = CENTER)
password.insert(0, 'Enter your password...')
password.bind('<FocusIn>', lambda event: temp_text_delete(password))

respond_password = CTkLabel(login_frame, 
                            bg_color ='transparent', 
                            text = '', 
                            font = ('Roboto', 12), 
                            wraplength = 380, 
                            justify = LEFT, 
                            height = 20, 
                            compound = LEFT)
respond_password.place(relx = 0.08, rely = 0.57, anchor = W)

login_button = CTkButton(login_frame, 
                         text = 'Log In', 
                         font = ('Roboto', 15, 'bold'),
                         command = check_password)
login_button.place(relx = button_x, rely = 0.7, anchor = CENTER)

sign_up_label = CTkLabel(login_frame, 
                         text = "Don't have an account yet? ", 
                         fg_color = 'transparent',
                         justify = LEFT,
                         font = ('Roboto', 15))
sign_up_label.place(relx = 0.05, rely = 0.9, anchor = W)

sign_up_button = CTkButton(login_frame, 
                           text = 'Sign up here', 
                           fg_color = 'transparent', 
                           bg_color = 'transparent',
                           text_color = ('black','white'),
                           font = ('Roboto', 14, 'bold'),
                           width = 20,
                           command = sign_up)
sign_up_button.place(relx = 0.45, rely = 0.854)

game_frame = CTkFrame(window, fg_color = ('#0a0838', '#3b3b3d'), border_width = 0)
game_frame.place(relx = game_frame_x, rely = 0.65, relwidth = 0.55, relheight = 0.7)

flappy_button = CTkButton(game_frame, 
                          text = 'Flappy Bird', 
                          font = ('Roboto', 20, 'bold'),
                          command = import_flappy)
flappy_button.place(relx = 0.25, rely = 0.25, anchor = CENTER)

snake_button = CTkButton(game_frame, 
                         text = 'Snake', 
                         font = ('Roboto', 20, 'bold'),
                         command = import_snake)
snake_button.place(relx = 0.75, rely = 0.25, anchor = CENTER)

shooter_button = CTkButton(game_frame, 
                           text = 'Shooter', 
                           font = ('Roboto', 20, 'bold'),
                           command = import_shooter)
shooter_button.place(relx = 0.25, rely = 0.75, anchor = CENTER)

tictactoe_button = CTkButton(game_frame, 
                             text = 'Tic-Tac-Toe', 
                             font = ('Roboto', 20, 'bold'),
                             command = import_tictactoe)
tictactoe_button.place(relx = 0.75, rely = 0.75, anchor = CENTER)

window.mainloop()
