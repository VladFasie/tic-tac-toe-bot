from game import TicTacToe
from helpers import board_to_neuron_inputs

from threading import Thread
from random import randint
import operator


class EvaluatorThread(Thread):

    def __init__(self, nn, iterations):
        Thread.__init__(self)
        self.nn = nn
        self.iterations = iterations
        self.score = 0

    def run(self):
        game = TicTacToe()
        print('started simulation')
        for _ in range(self.iterations):
            try:
                while not game.is_done():
                    data = board_to_neuron_inputs(game.board)
                    result = self.nn.feed_forward(data)
                    disponible_moves = game.disponible_moves()
                    sorted_result = sorted(enumerate(result), key=operator.itemgetter(1), reverse=True)
                    move = None
                    for idx_val in sorted_result:
                        idx = idx_val[0]
                        if idx in disponible_moves:
                            move = idx
                            break
                    game.move(move)
                    if not game.is_done():
                        disponible_moves = game.disponible_moves()
                        game.move(disponible_moves[randint(0, len(disponible_moves) - 1)])
            except:
                # ivalid move
                continue
            if game.winner == TicTacToe.X:
                self.score += 1
            elif game.winner == TicTacToe.O:
                self.score -= 1
            game.clear()
