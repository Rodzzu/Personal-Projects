from tkinter import *
win = Tk()

# Functionality

def addition():
    final.config(text= int(inp1.get()) + int(inp2.get()))

def subtract():
    final.config(text= int(inp1.get()) - int(inp2.get()))

def multiplication():
    final.config(text= int(inp1.get()) * int(inp2.get()))

def division():
    final.config(text= int(inp1.get()) / int(inp2.get()))

def floor():
    final.config(text= int(inp1.get()) // int(inp2.get()))

def exponent():
    final.config(text= int(inp1.get()) ** int(inp2.get()))

def modulo():
    final.config(text= int(inp1.get()) % int(inp2.get()))


# Labels

intro = Label(win, text= "Not A Calculator :3", font = ('Calibri', 25, 'bold'), fg= 'green')

num1 = Label(win, text= "Number 1", font = ('Corbel', 16), fg= 'blue')
num2 = Label(win, text= "Number 2", font = ('Corbel', 16), fg= 'blue')

result = Label(win, text = "Result:", font = ('Corbel', 16), fg= 'blue')
final = Label(win, text= '00', font= ('Corbel', 20)) # to display real result

# Text Box

inp1 = Entry(win, width= 27, font= ("Corbel", 16), fg= 'blue')
inp2 = Entry(win, width= 27, font= ("Corbel", 16), fg= 'blue')

# Buttons

add = Button(win, width= 4, text= "+", font = ('Corbel', 16, 'bold'), fg= 'blue', command= addition)
sub = Button(win, width= 4, text= "-", font = ('Corbel', 16, 'bold'), fg= 'blue', command= subtract)
mul = Button(win, width= 4, text= "x", font = ('Corbel', 16, 'bold'), fg= 'blue', command= multiplication)
div = Button(win, width= 4, text= "÷", font = ('Corbel', 16, 'bold'), fg= 'blue', command= division)
floordiv = Button(win, width= 4, text= "//", font = ('Corbel', 16, 'bold'), fg= 'blue', command= floor)
exp = Button(win, width= 4, text= "^", font = ('Corbel', 16, 'bold'), fg= 'blue', command= exponent)
modu = Button(win, width= 4, text= "%", font = ('Corbel', 16, 'bold'), fg= 'blue', command= modulo)

# Place

intro.place(x = 180, y = 60)

num1.place(x = 90, y = 170)
num2.place(x = 90, y = 210)

result.place(x = 90, y = 270)
final.place(x = 210, y = 265)

inp1.place(x = 200, y = 173)
inp2.place(x = 200, y = 213)

add.place(x = 90, y = 350)
sub.place(x = 150, y = 350)
mul.place(x = 210, y = 350)
div.place(x = 270, y = 350)
floordiv.place(x = 330, y = 350)
exp.place(x = 390, y = 350)
modu.place(x = 450, y = 350)

# Window Measurement

win.geometry("600x600+650+215")
win.title("Pseudo Calculator")
win.mainloop()