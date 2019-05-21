from nn import NeuralNetwork
from helpers import get_best_legal_move

from tkinter import *
from functools import partial
from game import TicTacToe
from tkinter import filedialog

master = Tk()
buttons = []
who_is_first_buttons = []
replay_btn = None

game = TicTacToe()
nn = None
X = PhotoImage(file='X.gif')
O = PhotoImage(file='O.gif')
Empty = PhotoImage(file='Empty.png')


def who_is_first(val):
    for b in who_is_first_buttons:
        b.grid_remove()
    who_is_first_buttons.clear()
    init_buttons()
    if val:
        bot_move()


def ask_who_is_first():
    you_first = Button(master, image=X, width=75, height=75, command=partial(who_is_first, False))
    bot_first = Button(master, image=O, width=75, height=75, command=partial(who_is_first, True))
    you_first.grid(row=1, column=1)
    bot_first.grid(row=1, column=2)
    who_is_first_buttons.append(you_first)
    who_is_first_buttons.append(bot_first)


def init_buttons():
    for i in range(3):
        for j in range(3):
            b = Button(master, image=Empty, width=55, height=55, command=partial(player_move, i, j))
            buttons.append(b)
            b.grid(row=i, column=j)


def load_bot():
    global nn
    filename = filedialog.askopenfilename(initialdir='/', title='Select file')
    nn = NeuralNetwork.load(filename)


def bot_move():
    idx = get_best_legal_move(nn, game)
    sign = game.next
    game.move(idx)
    update_ui(idx, sign)


def player_move(i, j):
    idx = i * 3 + j
    sign = game.next
    game.move(idx)
    update_ui(idx, sign)
    if not game.is_done():
        bot_move()


def update_ui(idx, sign):
    global replay_btn
    if sign == TicTacToe.X:
        img = X
    else:
        img = O
    buttons[idx].configure(image=img, state='disabled')
    if game.is_done():
        for b in buttons:
            b.configure(state='disabled')
        replay_btn = Button(master, text='replay', command=reset)
        replay_btn.grid(row=3, column=1)


def reset():
    for b in buttons:
        b.grid_remove()
    buttons.clear()
    game.clear()
    replay_btn.grid_remove()
    ask_who_is_first()


load_bot()
ask_who_is_first()
mainloop()
