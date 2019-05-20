
class TicTacToe:

    X = 'X'
    O = 'O'
    Empty = ' '

    def __init__(self):
        self.board = [TicTacToe.Empty for _ in range(9)]
        self.next = TicTacToe.X
        self.winner = TicTacToe.Empty
        self.round = 0

    def is_done(self):
        return self.round == 9 or self.winner != TicTacToe.Empty

    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == TicTacToe.Empty]

    def move(self, pos):
        if self.is_done():
            raise Exception('game already finished')
        if self.board[pos] != TicTacToe.Empty:
            raise Exception('invalid move at position {}'.format(pos))
        self.board[pos] = self.next
        if self.next == TicTacToe.X:
            self.next = TicTacToe.O
        elif self.next == TicTacToe.O:
            self.next = TicTacToe.X
        else:
            raise Exception('wrong next player {}'.format(self.next))
        self.round += 1
        self.check_winner()

    def check_winner(self):
        if self.round < 5:
            return
        # rows check
        for i in range(0, 9, 3):
            if self.board[i] != TicTacToe.Empty and \
                    self.board[i + 1] == self.board[i + 2] and \
                    self.board[i] == self.board[i + 1]:
                self.winner = self.board[i]
                return
        for i in range(3):
            if self.board[i] != TicTacToe.Empty and \
                    self.board[i + 3] == self.board[i + 6] and \
                    self.board[i] == self.board[i + 3]:
                self.winner = self.board[i]
                return
        if self.board[4] != TicTacToe.Empty:
            if self.board[0] == self.board[8] and self.board[4] == self.board[0]:
                self.winner = self.board[4]
                return
            if self.board[2] == self.board[6] and self.board[4] == self.board[2]:
                self.winner = self.board[4]
                return

    def clear(self):
        self.board = [TicTacToe.Empty for _ in range(9)]
        self.next = TicTacToe.X
        self.winner = TicTacToe.Empty
        self.round = 0

    def __str__(self):
        result = ''
        for i in range(0, 9, 3):
            result += self.board[i] + '|' + self.board[i + 1] + '|' + self.board[i + 2]
            result += '\n'
        return result
