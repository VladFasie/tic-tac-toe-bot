from helpers import get_best_legal_move
from bit_game import BitTicTacToe

from random import randint


def simulate(nn, iterations):
    score = 0
    game = BitTicTacToe()
    half_iterations = int(iterations / 2)
    for _ in range(half_iterations):
        result = simulate_nn_first(nn, game)
        if result == BitTicTacToe.X:
            score += 1
        elif game.winner == BitTicTacToe.O:
            score -= 1
        game.clear()
    for _ in range(half_iterations):
        result = simulate_nn_second(nn, game)
        if result == BitTicTacToe.O:
            score += 1
        elif game.winner == BitTicTacToe.X:
            score -= 1
        game.clear()
    return score


def simulate_nn_first(nn, game):
    # assumption game is not done
    while True:
        move_nn(game, nn)
        if game.is_done():
            break
        move_random(game)
        if game.is_done():
            break
    return game.winner


def simulate_nn_second(nn, game):
    # assumption game is not done
    while True:
        move_random(game)
        if game.is_done():
            break
        move_nn(game, nn)
        if game.is_done():
            break
    return game.winner


def move_random(game):
    # not checked if move is possible
    available_moves = game.available_moves()
    game.move(available_moves[randint(0, len(available_moves) - 1)])


def move_nn(game, nn):
    # not checked if move is possible
    move = get_best_legal_move(nn, game)
    game.move(move)
