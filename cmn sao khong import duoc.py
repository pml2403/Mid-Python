from customtkinter import *

window = CTk()
window.geometry('200x200')

def import_flappy():
    import flappybird_main

def import_snake():
    import snake_main

def import_shooter():
    import shooter_main

def import_tictactoe():
    import tictactoe_main

button_1 = CTkButton(window, text = 'flappy', command = import_flappy)
button_2 = CTkButton(window, text = 'snake', command = import_snake)
button_3 = CTkButton(window, text = 'shooter', command = import_shooter)
button_4 = CTkButton(window, text = 'tictactoe', command = import_tictactoe)

button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()

window.mainloop()