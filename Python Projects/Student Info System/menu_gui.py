import tkinter
from tkinter import *
from functools import partial
from add_student import *

win = Tk()
btns = []
stud = StudentInfo()
addStud = AddStudent(stud)

NormalStudent = addStud.add_student('Rodney', '19', '2023-2-02298', '2023-2-02298@gmail.com', '09999234567')

# Functions

def func1():
    print('Button 1')

def func2():
    print('Button 2')

def func3():
    print('Button 3')
def func4():
    print('Button 4')

def func5():
    print('Button 5 ')

def login():
    # if block for verifying login

    attempts = 0

    if stud.login(id.get()):
        login_frame.pack_forget()
        menu_contain.pack(side='left', fill='y')
        content_contain.pack(side='left', fill='x')
    else:
        attempts += 1
        Label(float_frame, text="This ID does not exist.", font=('Century Gothic', 20), padx=20).pack()

        if attempts == 4:
            Label(float_frame, text="You have reached the maximum attempts.", font=('Century Gothic', 20), padx=20).pack()

def logout():
    menu_contain.pack_forget()
    content_contain.pack_forget()
    login_frame.pack(fill= 'both', expand= True)
    id.delete(0, tkinter.END)

btn_txt = ['Button 1', 'Button 2', 'Button 3', 'Button 4', 'Button 5', 'Logout']

func = [func1, func2, func3, func4, func5, logout]

# Login
login_frame = Frame(win, bg = "white")

# Floating Window for Login

float_frame = Frame(login_frame, bg = "lightblue", padx= 20, pady = 10, relief= 'solid')
Label(float_frame, text= "Login to continue", font = ('Century Gothic', 20), padx = 20).pack()
id = Entry(float_frame, width = 20, font= ('Century Gothic', 20))
login_btn = Button(float_frame, text= "Login", width= 20, font= ('Century Gothic', 20), command = login, relief= 'groove')

# Main Frame

main_frame = Frame(win, bg = "white")
Label(main_frame, text = 'Main', font= ('Century Gothic', 20), padx= 20).pack()

# Frame Creation

menu_contain = Frame(win, borderwidth= 0, bg= "#70909C", relief= 'solid')
content_contain = Frame(win, borderwidth= 1, bg= 'white')
Label(menu_contain, text= "Main Menu", font= ('Century Gothic', 30), fg= 'white', bg= '#70909C', border= 0, pady= 70).grid(row= 0, column=0, sticky= 'ew')
logout_btn = Button(menu_contain, text= 'Logout', width= 40, font= ('Century Gothic', 14), command = logout)

# Button Creation

for i, txt in enumerate(btn_txt):
    btns.append(Button(menu_contain, width= 40, text = btn_txt[i], font= ('Century Gothic', 14), padx= 10, pady= 15, bg = 'white', relief= 'flat'))

for i in range(len(btns)): # Places the buttons in the grid.
    btns[i].grid(row = i+1, column= 0, sticky= 'ew', pady= 5)

for i in range(len(btns)): # Configures the buttons to call the functions
    btns[i].config(command= partial(func[i]))

# Packing/Placing
login_frame.pack(fill= 'both', expand= True)
float_frame.place(relx = 0.5, rely = 0.5, anchor= 'center')
Label(float_frame, text = 'Enter ID:', font = ('Century Gothic', 20), padx= 20).pack()
id.pack()
login_btn.pack()

# Window
win.geometry('1280x800+320+140')
win.title('Student Information System')
win.mainloop()