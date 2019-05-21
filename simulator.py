from helpers import get_best_legal_move, get_best_move
from bit_game import BitTicTacToe

from random import randint

win_score = 1
loss_score = -1
wrong_move_penalty = -10

def simulate(nn, iterations):
    score = 0
    game = BitTicTacToe()
    half_iterations = int(iterations / 2)
    for _ in range(half_iterations):
        score += simulate_nn_first(nn, game)
        game.clear()
    for _ in range(half_iterations):
        score += simulate_nn_second(nn, game)
        game.clear()
    return score


def simulate_nn_first(nn, game):
    # assumption game is not done
    while True:
        if not move_nn(game, nn):
            return game.round + wrong_move_penalty
        if game.is_done():
            break
        move_random(game)
        if game.is_done():
            break
    if game.winner == BitTicTacToe.X:
        return win_score
    elif game.winner == BitTicTacToe.O:
        return loss_score


def simulate_nn_second(nn, game):
    # assumption game is not done
    while True:
        move_random(game)
        if game.is_done():
            break
        if not move_nn(game, nn):
            return game.round + wrong_move_penalty
        if game.is_done():
            break
    if game.winner == BitTicTacToe.X:
        return loss_score
    elif game.winner == BitTicTacToe.O:
        return win_score


def move_random(game):
    # not checked if move is possible
    available_moves = game.available_moves()
    game.move(available_moves[randint(0, len(available_moves) - 1)])


def move_nn(game, nn):
    # not checked if move is possible
    #move = get_best_legal_move(nn, game)
    move = get_best_move(nn, game)
    if move in game.available_moves():
        game.move(move)
        return True
    return False
