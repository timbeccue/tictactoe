
import unittest
from board import Board

PRINT = False
def _print(to_print):
    if PRINT: print(to_print)


class Test_Board(unittest.TestCase):

    def setUp(self):
        _print("testing: setup")
        self.board = Board()

    def test_initialize_board(self):
        _print("testing: initialize board")
        board_to_test = self.board.get_board()
        self.assertTrue(sum(len(row) for row in board_to_test), 9)

    def test_play(self):
        _print("testing: playing 3 moves")
        for i in range(3):
            self.board.play(1,i,i)
        board_to_test = self.board.get_board()
        self.assertTrue(sum(map(sum,board_to_test)), 3)

    def test_check_win_diagonal(self):
        _print("testing: checking diagonal win status")
        player = 'x'
        for i in range(3):
            self.board.play(player,i,i)
        self.assertEqual(self.board.check_win(), player)

    def test_check_win_row(self):
        _print("testing: checking row win status")
        player = 'y'
        for i in range(3):
            self.board.play(player,1,i)
        self.assertEqual(self.board.check_win(), player)

    def test_check_win_col(self):
        _print("testing: checking column win status")
        player = 'z'
        for i in range(3):
            self.board.play(player,i,1)
        self.assertEqual(self.board.check_win(), player)

    def test_check_open_space(self):
        _print("testing: checking open spaces")
        player = 'x'
        for i in range(3):
            self.board.play(player,i,i)
        self.assertFalse(self.board.check_open_space(0,0))
        self.assertTrue(self.board.check_open_space(0,1))

if __name__=='__main__':
    unittest.main()
