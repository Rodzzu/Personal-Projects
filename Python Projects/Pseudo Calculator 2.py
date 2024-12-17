from tkinter import *
from functools import partial
win = Tk()
btns = ['**', '//', '%', 'C', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '/', '.', '0', '=', '*',]
def new(x):
    if res.cget("text") == "0" and x not in ["C", "="]:
        res.config(text=x)
    elif x == "=":
        res.config(text= str(eval(res.cget("text"))))
    elif x == "C":
        res.config(text="0")
    else:
        res.config(text=res.cget("text") + x)
row_num = 0
col_num = 0
res = Label(win, text="0", font=('Helvetica', 26), fg='white', bg='black', anchor="e", width=15)
res.grid(row=0, column=0, columnspan=4, sticky="we")
for i in range(len(btns)):
    Button(win, width=4, text=btns[i], font=('Helvetica', 24), fg='white', bg='gray', activebackground='darkgray', activeforeground='white', command=partial(new, btns[i])).grid(row= row_num + 2, column= col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0
win.configure(bg='black')
win.geometry("372x408+774+336")
win.title("Pseudo Calculator 2")
(win.mainloop())