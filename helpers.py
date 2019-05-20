from game import TicTacToe
from nn import NeuralNetwork

from random import randint


def board_to_neuron_inputs(board):
    xs = []
    os = []
    for item in board:
        if item == TicTacToe.X:
            xs.append(1)
            os.append(0)
        elif item == TicTacToe.O:
            xs.append(0)
            os.append(1)
        else:
            xs.append(0)
            os.append(0)
    return xs + os


def choose(a, b):
    if randint(0, 1) == 0:
        return a
    else:
        return b


def generate_nn():
    return NeuralNetwork(18, [
        [16, 'sigmoid'],
        [9, 'sigmoid']
    ])
