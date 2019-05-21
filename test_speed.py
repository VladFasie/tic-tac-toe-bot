from bit_game import BitTicTacToe
from game import TicTacToe
from simulator import move_random
from time import time
from random import randint

n = 100000

normal_game = BitTicTacToe()
bit_game = TicTacToe()


def test(game, iterations):
    start = time()
    for _ in range(iterations):
        while not game.is_done():
            move_random(game)
        game.clear()
    stop = time()
    print(stop - start)


def games_are_equivalent():
    a = TicTacToe()
    b = BitTicTacToe()
    for i in range(10000):
        while True:
            ma = a.available_moves()
            mb = b.available_moves()
            if not sorted(ma) == sorted(mb):
                raise Exception()
            m = ma[randint(0, len(ma) - 1)]
            a.move(m)
            b.move(m)
            if a.is_done() != b.is_done():
                raise Exception()
            if not ((a.winner == TicTacToe.X and b.winner == BitTicTacToe.X) or
                    (a.winner == TicTacToe.O and b.winner == BitTicTacToe.O) or
                    (a.winner == TicTacToe.Empty and b.winner == BitTicTacToe.Empty)):
                raise Exception()
            if a.is_done():
                break
        a.clear()
        b.clear()


test(normal_game, n)
test(bit_game, n)

#games_are_equivalent()
