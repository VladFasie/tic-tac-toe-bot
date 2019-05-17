from game import TicTacToe
from nn import NeuralNetwork
import operator
from random import randint


def generate_nn():
    return NeuralNetwork(18, [
        #[18, 'sigmoid'],
        [16, 'sigmoid'],
        #[14, 'sigmoid'],
        #[12, 'sigmoid'],
        #[10, 'sigmoid'],
        [9, 'sigmoid']
    ])

n = 20
k = 10000
nns = {}
for i in range(n):
    nns[generate_nn()] = 0

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

#nn.unbind_neurons(0, 0, 1)
#nn.unbind_neurons(0, 2, 0)
#nn.unbind_neurons(1, 1, 0)

#for i in nn.layers:
#    print(i)

def test():
    game = TicTacToe()
    loop_idx = 0
    for nn in nns:
        print(loop_idx)
        loop_idx += 1
        for _ in range(k):
            game.clear()
            try:
                while not game.is_done():
                    data = board_to_neuron_inputs(game.board)
                    result = nn.feed_forward(data)
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
                continue
            if game.winner == TicTacToe.X:
                nns[nn] += 1
            elif game.winner == TicTacToe.O:
                nns[nn] -= 1

    sorted_nns = sorted(nns.items(), key=operator.itemgetter(1))

    print(sorted_nns)

test()