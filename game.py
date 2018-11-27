
import random
from board import Board
from players import HumanPlayer, RandomPlayer
from itertools import cycle

PRINT = True
def _print(toprint):
    if PRINT: print(toprint)

class Game:

    def __init__(self):
        self.board = Board()
        self.p_turn = cycle(range(2))

    def add_players(self, player1, player2):
        self.players = [player1, player2]
        # randomize player 1
        if random.getrandbits(1): next(self.p_turn)
        # set player tokens
        self.tokens = ['A', 'B']
        self.players[0].set_token('A')
        self.players[1].set_token('B')

    def play(self):

        winner = 0
        turn = 0
        while winner is 0 and turn < 9:
            _print(f"Turn {turn}: ")
            #_print(self.board.printable_board())
            player_idx = next(self.p_turn)
            player = self.players[player_idx]
            row, col = player.play(self.board)
            if self.board.check_open_space(row,col):
                self.board.play(self.tokens[player_idx], row, col)
            winner = self.board.check_win()
            turn += 1
        _print(f"Winner is {winner}!")
        _print(self.board.printable_board())
        return winner


if __name__=='__main__':
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    game = Game()
    game.add_players(player1, player2)
    game.play()
