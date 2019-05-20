from game import TicTacToe
from helpers import get_best_legal_move

from random import randint


def simulate(nn, iterations):
    score = 0
    game = TicTacToe()
    for _ in range(iterations):
        try:
            while not game.is_done():
                move = get_best_legal_move(nn, game)
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
