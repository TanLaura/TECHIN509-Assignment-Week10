import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def test_winner_in_row(self):
        board = Board()
        board.grid = [["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]
        self.assertEqual(board.check_winner(), "X")

    def test_winner_in_column(self):
        board = Board()
        board.grid = [[" ", "O", "X"], [" ", "O", "X"], [" ", " ", "X"]]
        self.assertEqual(board.check_winner(), "X")

    def test_winner_in_diagonal(self):
        board = Board()
        board.grid = [["O", " ", "X"], [" ", "X", " "], ["X", "O", " "]]
        self.assertEqual(board.check_winner(), "X")

    def test_no_winner(self):
        board = Board()
        board.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertEqual(board.check_winner(), "")

if __name__ == "__main__":
    unittest.main()