from nn import NeuralNetwork
from helpers import get_best_legal_move

from tkinter import *
from functools import partial
from game import TicTacToe
from tkinter import filedialog

master = Tk()
buttons = []
replay_btn = None

game = TicTacToe()
nn = None
X = PhotoImage(file='X.gif')
O = PhotoImage(file='O.gif')
Empty = PhotoImage(file='Empty.png')


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
    game.move(idx)
    update_ui(idx)


def player_move(i, j):
    idx = i * 3 + j
    game.move(idx)
    update_ui(idx)
    if not game.is_done():
        bot_move()


def update_ui(idx):
    global replay_btn
    if game.next == TicTacToe.X:
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
        b.configure(image=Empty, state='normal')
    game.clear()
    if replay_btn is not None:
        replay_btn.grid_remove()
    bot_move()


load_bot()
init_buttons()
bot_move()
mainloop()
