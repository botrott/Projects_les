import tkinter as tk
from tkinter import messagebox
from random import choice
from datetime import datetime

def congratulation(name):
    list_one_word = ["активности", "бодрости", "везения", "вдохновения", "взаимности", "внимания", "возможностей",
                     "восторга", "впечатлений", "добра", "достатка", "доходов", "драйва", "душевности", "заботы",
                     "задора", "изобилия", "карьеры", "комфорта", "легкости", "мира", "отдыха", "открытий", "оптимизма",
                     "перемен", "подарков", "позитива", "понимания", "признания", "путешествий", "радости",
                     "развлечений",
                     "романтики", "роскоши", "роста", "свершений", "свободы", "сил", "совершенства", "спокойствия",
                     "сюрпризов",
                     "удачи", "улыбки", "уюта", "энергии", "тепла"]

    list_one_string = ["удачи во всем!", "благополучия во всем!", "бодрости духа", "больших успехов",
                       "ярких и крутых событий",
                       "море веселья!", "возможностей для отдыха!", "высоких доходов", "добра и позитива",
                       "железной мотивации",
                       "интересных идей", "крутых путешествий", "крутых достижений", "легкого отношения к жизни",
                       "больше улыбок",
                       "максимум позитива", "нескучной повседневности", "неиссякаемой энергии", "новых возможностей",
                       "море новых впечатлений",
                       "отличного настроения", "побольше свободного времени", "творческого вдохновения",
                       "хорошего настроения", "хороших перемен",
                       "ярких ощущений"]

    return f'{name}, Поздравляю тебя С Днём Рождения! Желаю; {choice(list_one_word)}, {choice(list_one_word)}, и {choice(list_one_string)}'


def wind():
    name = EnterText.get()
    text = congratulation(name)
    EnterText.delete(0, 'end')
    AnswerText.delete('1.0', 'end')
    AnswerText.insert('1.0', text)


def EnterClick(enter):
    wind()


window = tk.Tk()
window.title('BirthDay')
window.geometry('470x350')
window.resizable(width=False, height=False)
window['bg'] = 'black'

Name = tk.Label(window, text='Введите имя', font=('arial bold', 15), fg='lime', bg='black')
Name.place(x=160, y=20)

EnterText = tk.Entry(fg='black', width=20)
EnterText.place(x=150, y=60)

btn = tk.Button(window, text='Поздравление', command=wind, fg='black', bg='white', width=18, height=1)
btn.place(x=150, y=100)

window.bind('<Return>', EnterClick)

AnswerText = tk.Text(window, font=('arial bold', 15), fg='lime', bg='black', width=25, height=5)
AnswerText.place(x=69, y=150)



window.mainloop()

