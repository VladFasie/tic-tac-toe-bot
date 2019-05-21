
class BitTicTacToe:

    X = 0b01
    O = 0b10
    Empty = 0b00

    def __init__(self):
        self.board = 0
        self.next = BitTicTacToe.X
        self.winner = BitTicTacToe.Empty
        self.round = 0

    def is_done(self):
        return self.round == 9 or self.winner != BitTicTacToe.Empty

    def available_moves(self):
        result = []
        k = 8
        for i in range(0, 18, 2):
            if (self.board >> i) & 0b11 == BitTicTacToe.Empty:
                result.append(k)
            k -= 1
        return result

    def move(self, pos):
        if self.is_done():
            raise Exception('game already finished')
        if (self.board >> (16 - 2 * pos) & 0b11) != BitTicTacToe.Empty:
            raise Exception('invalid move at position {}'.format(pos))
        self.board = self.board | (self.next << (16 - 2 * pos))
        self.next ^= 0b11
        self.round += 1
        self.check_winner()

    def check_winner(self):
        if self.round < 5:
            return
        # rows check
        for i in range(12, -1, -6):
            tmp = (self.board >> i) & 0b111111
            if tmp & 0b11 != BitTicTacToe.Empty and \
                    tmp & 0b11 == (tmp >> 2) & 0b11 and \
                    tmp & 0b11 == (tmp >> 4) & 0b11:
                self.winner = tmp & 0b11
                return
        # column check
        for i in range(16, 11, -2):
            tmp = (self.board >> i) & 0b11
            if tmp != BitTicTacToe.Empty and \
                    tmp == (self.board >> (i - 6)) & 0b11 and \
                    tmp == (self.board >> (i - 12)) & 0b11:
                self.winner = tmp
                return
        center = (self.board >> 8) & 0b11
        if center != BitTicTacToe.Empty:
            if center == self.board & 0b11 and (center == self.board >> 16) & 0b11:
                self.winner = center
                return
            if center == (self.board >> 4) & 0b11 and center == (self.board >> 12) & 0b11:
                self.winner = center
                return

    def clear(self):
        self.board = 0
        self.next = BitTicTacToe.X
        self.winner = BitTicTacToe.Empty
        self.round = 0

    def to_nn_input(self):
        xs = []
        os = []
        for i in range(16, -1, -2):
            tmp = (self.board >> i) & 0b11
            if tmp == BitTicTacToe.X:
                xs.append(1)
                os.append(0)
            elif tmp == BitTicTacToe.O:
                xs.append(0)
                os.append(1)
            else:
                xs.append(0)
                os.append(0)
        return xs + os
