from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('500x200')
window.title('GAME STATION')

title = Label(window, 
              text = 'GAME STATION', 
              font = ('Helvetica', 30, 'bold'), 
              fg = 'orangered2')
title.pack()
#title.place(relx = 0.5, rely = 0.5, anchor=CENTER)

canvas = Canvas(window, width = 500, height = 200)
canvas.pack()

login_frame = Frame(canvas, width = 100, height = 100, padx = 0, pady = 0)
frame_id = canvas.create_window(0, 100, window=login_frame, anchor= NW)
login_frame.pack(side = TOP)

names = ['mailinh@gmail.com', 'baophung@gmail.com', 'leduy@gmail.com', 'lethao@gmail.com']

def temp_text_login():
    login_name.delete(0, END)

def temp_text_password():
    password.delete(0, END)
    password.config(show = '*')

def go_to_next_entry():
    password.focus_set()

def check_name(event):
    if login_name.get() in names:
        print('Valid name!')
        go_to_next_entry()
    else:
        print('Invalid name')

login_name = Entry(login_frame,
                   font = ('Arial', 15))
login_name.insert(0, 'Enter your email...')
login_name.bind('<FocusIn>', lambda event: temp_text_login()) #vì truyền tham số vào nên nó sẽ trigger luôn cái func chứ không đợi event xảy ra
login_name.bind("<Return>", check_name)

password = Entry(canvas, font = ('Arial', 15))
password.insert(0, 'Enter your password...')
password.bind('<FocusIn>', lambda event: temp_text_password())

submit_button = Button(canvas, text = 'Submit', font = ('Arial', 15))

login_name.pack()
password.pack()
submit_button.pack()

window.mainloop()