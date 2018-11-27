
PRINT = False
def _print(to_print):
    if PRINT: print(to_print)


# board is indexed as (row, column).
#   [ [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0] ]

class Board:

    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[0 for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]

    def reset_board(self):
        self.board = [[0 for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]

    def check_open_space(self, row, column):
        return self.board[row][column] == 0

    def play(self, player, row, column):
        self.board[row][column] = player

    def check_win(self):
        winning_player = 0
        _print(self.board)
        for i in range(self.BOARD_SIZE):
            # Check rows
            if 0 != self.board[i][0] == self.board[i][1] == self.board[i][2]:
                winning_player = self.board[i][0]
            # Check columns
            if 0 != self.board[0][i] == self.board[1][i] == self.board[2][i]:
                winning_player = self.board[0][i]

        # Check diagonals
        if 0 != self.board[0][0] == self.board[1][1] == self.board[2][2]:
            winning_player = self.board[1][1]
        if 0 != self.board[0][2] == self.board[1][1] == self.board[2][0]:
            winning_player = self.board[1][1]

        return winning_player

    def get_board(self):
        _print(self.board)
        return self.board

    def print_board(self):
        pretty_board = f"""
        -----------
        | {self.board[0][0]}  {self.board[0][1]}  {self.board[0][2]} |
        | {self.board[1][0]}  {self.board[1][1]}  {self.board[1][2]} |
        | {self.board[2][0]}  {self.board[2][1]}  {self.board[2][2]} |
        -----------
        """
        print(pretty_board)