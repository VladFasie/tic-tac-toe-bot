from game import TicTacToe
from helpers import board_to_neuron_inputs

from random import randint
import operator


def simulate(nn, iterations):
    score = 0
    game = TicTacToe()
    for _ in range(iterations):
        try:
            while not game.is_done():
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
                game.move(move)
                if not game.is_done():
                    available_moves = game.available_moves()
                    game.move(available_moves[randint(0, len(available_moves) - 1)])
        except:
            # invalid move
            continue
        if game.winner == TicTacToe.X:
            score += 1
        elif game.winner == TicTacToe.O:
            score -= 1
        game.clear()
    return score
