
import random

PRINT = True
def _print(toprint):
    if PRINT: print(toprint)

class HumanPlayer:

    # Allow game to define player token (eg. X or O)
    def set_token(self, token):
        self.token = token

    def play(self, board):
        _print(board.printable_board())
        row = col = 0

        # player mechanics go here
        row = int(input(f"Enter row: "))
        col = int(input(f"Enter col: "))

        return (row, col)

class RandomPlayer:

    def set_token(self, token):
        pass
    def play(self, board):
        available = []
        for row in range(3):
            for col in range(3):
                if board.check_open_space(row, col):
                    available.append((row,col))
        _print(f"available: {available}, length: {len(available)}")
        return available[random.randint(0, len(available)) - 1]
