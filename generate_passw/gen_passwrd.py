from tkinter import *
from random import choice

def random():
    lenPassword = field.get()       # сохраняется в переменную
    field.delete(0, END)            # очистить поле
    for i in range(int(lenPassword)):
        field.insert(0, choice(aph))      # от 0, до конца alf


root = Tk()
root.title('Generate_password')
root.geometry('300x200')
root.resizable(width=False, height=False)

aph = ['1', '2', '3', 'a', 'b', 'c', 'd']


field =  Entry(root, font='arial 13')                 # поле для ввода, сколько символов, пользователь хочет, чтобы было в его пароле
field.place(relx=0.5, y=20, anchor=CENTER)


btn = Button(root, command=random, text='Generate', font='arial, 15')
btn.place(relx=0.5, y=70, anchor=CENTER)

root.mainloop()