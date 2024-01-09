import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fourtic

def test_play2():
	b = fourtic.Board(file="./boards/play-2.txt")
	assert b.evalInitState() == ("X", 2)

def test_play5():
	b = fourtic.Board(file="./boards/play-5.txt")
	assert b.evalInitState() == ("O", 5)

def test_rand4():
	b = fourtic.Board(file="./boards/rand-4.txt")
	assert b.evalInitState() == ("X", 4)

def test_rand7():
	b = fourtic.Board(file="./boards/rand-7.txt")
	assert b.evalInitState() == ("O", 7)
