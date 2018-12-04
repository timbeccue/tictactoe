
PRINT = True
def _print(to_print):
    if PRINT: print(to_print)


# board is indexed as (row, column).
#   [ [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0] ]

class Board:

    def __init__(self, board_size=3):
        self.board_size = 3
        self.board = [[0 for i in range(self.board_size)] for j in range(self.board_size)]

    def check_open_space(self, row, col, board=0):
        if board is 0: board = self.board
        size = len(board)
        if row > size-1 or row < 0: return False
        if col > size-1 or col < 0: return False
        return board[row][col] == 0

    def check_win(self, board=0):
        if board is 0: board = self.board
        size = len(board)
        winning_player = 0
        _print(board)
        for i in range(size):
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
        self.board = [[0 for i in range(self.board_size)] for j in range(self.board_size)]

    def get_board(self):
        _print(self.board)
        return self.board

    def printable_board(self, board=0):
        if board is 0: board = self.board
        pretty_board = f"""
        -----------
        | {board[0][0]}  {board[0][1]}  {board[0][2]} |
        | {board[1][0]}  {board[1][1]}  {board[1][2]} |
        | {board[2][0]}  {board[2][1]}  {board[2][2]} |
        -----------
        """
        return(pretty_board)
