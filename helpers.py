from game import TicTacToe


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
