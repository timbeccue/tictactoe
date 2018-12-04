
import random
from board import Board as gb

PRINT = True
def _print(toprint):
    if PRINT: print(toprint)

class HumanPlayer:

    # Allow game to define player token (eg. X or O)
    def set_token(self, token, opponent):
        self.token = token
        self.opponent = opponent

    def play(self, board):
        _print(board.printable_board())
        row = col = 0

        # player mechanics go here
        row = int(input(f"Enter row: "))
        col = int(input(f"Enter col: "))

        return (row, col)

class RandomPlayer:

    def set_token(self, token, opponent):
        pass
    def play(self, board):
        available = []
        for row in range(3):
            for col in range(3):
                if board.check_open_space(row, col):
                    available.append((row,col))
        return available[random.randint(0, len(available)) - 1]

class PerfectPlayer:

    def __init__(self):
        self.gb = gb() # for static methods only

    def set_token(self, token, opponent):
        self.token = token
        self.opponent = opponent

    def play(self, board):
        self._save_current_game_board(board)
        row = col = 0

        available_moves = self._get_available_moves(self.current_board)

        # No decision needed if only one move is possible
        if len(available_moves) is 1:
            return available_moves[0]

        # Win if possible
        move = self._search_winning_moves(self.current_board, available_moves)
        if move: return move

        # Prevent loss if imminent
        move = self._search_prevent_loss(self.current_board, available_moves)
        if move: return move

        # Play center if open
        if (1,1) in available_moves:
            return (1,1)

        # Play corner if open
        for corner in [(0,0), (0,2), (2,0), (2,2)]:
            if corner in available_moves:
                return corner

        # Else, play random
        return available_moves[random.randint(0, len(available)) - 1]

    def _save_current_game_board(self, board):
        self.current_board = board.get_board()

    def _get_available_moves(self, game_board):
        available = []
        size = len(game_board)
        for row in range(size):
            for col in range(size):
                if self.gb.check_open_space(row, col, game_board):
                    available.append((row, col))
        return available

    def _search_winning_moves(self, game_board, available):
        for move in available:
            possible_board = game_board
            possible_board[move[0]][move[1]] = self.token
            if self.gb.check_win(possible_board) == self.token:
                return move
        return False

    def _search_prevent_loss(self, game_board, available):
        for move in available:
            possible_board = game_board
            possible_board[move[0]][move[1]] = self.opponent
            if self.gb.check_win(possible_board) == self.opponent:
                return move
        return False
