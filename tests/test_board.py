import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fourtic

def test_play2():
	b = fourtic.Board("./boards/play-2.txt")
	board = [[".", "X", "O", "X"],
			 ["O", "X", "O", "O"],
			 [".", "X", "O", "O"],
			 ["X", "X", "X", "O"]]
	assert b.board == board

def test_play7():
	b = fourtic.Board("./boards/play-7.txt")
	board = [["X", ".", ".", "."],
			 ["O", ".", ".", "X"],
			 ["X", ".", ".", "X"],
			 ["O", "O", "X", "O"]]
	assert b.board == board
