
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

    def check_open_space(self, row, col):
        if row > self.BOARD_SIZE-1 or row < 0: return False
        if col > self.BOARD_SIZE-1 or col < 0: return False
        return self.board[row][col] == 0

    def check_win(self, board=0):
        if board is 0: board = self.board
        winning_player = 0
        _print(board)
        for i in range(self.BOARD_SIZE):
            # Check rows
            if 0 != board[i][0] == board[i][1] == board[i][2]:
                winning_player = board[i][0]
            # Check columns
            if 0 != board[0][i] == board[1][i] == board[2][i]:
                winning_player = board[0][i]

        # Check diagonals
        if 0 != board[0][0] == board[1][1] == board[2][2]:
            winning_player = board[1][1]
        if 0 != board[0][2] == board[1][1] == board[2][0]:
            winning_player = board[1][1]

        return winning_player

    def play(self, player, row, column):
        if self.check_open_space(row, column):
            self.board[row][column] = player

    def reset_board(self):
        self.board = [[0 for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]

    def get_board(self):
        _print(self.board)
        return self.board

    def printable_board(self):
        pretty_board = f"""
        -----------
        | {self.board[0][0]}  {self.board[0][1]}  {self.board[0][2]} |
        | {self.board[1][0]}  {self.board[1][1]}  {self.board[1][2]} |
        | {self.board[2][0]}  {self.board[2][1]}  {self.board[2][2]} |
        -----------
        """
        return(pretty_board)
