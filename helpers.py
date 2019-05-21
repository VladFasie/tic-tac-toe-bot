from game import TicTacToe
from nn import NeuralNetwork

from random import randint
import operator


def choose(a, b):
    if randint(0, 1) == 0:
        return a
    else:
        return b


def get_best_legal_move(nn, game):
    data = game.to_nn_input()
    result = nn.feed_forward(data)
    available_moves = game.available_moves()
    sorted_result = sorted(enumerate(result), key=operator.itemgetter(1), reverse=True)
    move = None
    for idx_val in sorted_result:
        idx = idx_val[0]
        if idx in available_moves:
            move = idx
            break
    return move


def generate_nn():
    return NeuralNetwork(18, [
        [16, 'sigmoid'],
        [14, 'sigmoid'],
        [12, 'sigmoid'],
        [9, 'sigmoid']
    ])
