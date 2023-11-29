from customtkinter import *
from random import choice
import tkinter

window = CTk()
window.geometry('500x600')
window.title('GAME STATION')

names = ['mailinh@gmail.com', 'baophung@gmail.com', 'leduy@gmail.com', 'lethao@gmail.com'] 
passwords = ['123456', '223456', '322456', '422456']

#functions
def temp_text_delete(thing):
    thing.delete(0, END)
    thing.configure(text_color = 'black')
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
        respond_password.configure(text = '')
        turn_to_game_page()

def turn_to_game_page():
    global button_x, done_moving_frame
    button_x -= 0.03
    login_frame.place(relx = button_x, rely = 0.6, anchor = CENTER)

    if button_x > -1.2:
        window.after(10, turn_to_game_page)
    else:
        move_game_in()



button_x = 0.5

title = CTkLabel(window, text = 'GAME STATION', 
                 font = ('Arial', 60, 'bold'), 
                 text_color = '#023ebf')
title.place(relx = 0.5, rely = 0.2, anchor='center')

login_frame = CTkFrame(window, width = 450, height = 300)
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

game_frame = CTkFrame(window, relx = 0.5, rely = 0.5, relwidth = 0.8, relheight = 0.9)

window.mainloop()
