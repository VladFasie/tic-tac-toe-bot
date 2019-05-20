from game import TicTacToe
from nn import NeuralNetwork

from random import randint
import operator

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


def get_best_legal_move(nn, game):
    data = board_to_neuron_inputs(game.board)
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
        [9, 'sigmoid']
    ])
