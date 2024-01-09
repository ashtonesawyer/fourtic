import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fourtic

def test_rand2():
	b = fourtic.Board(file="./boards/rand-2.txt")
	(score, move) = b.negamax(b.player)
	assert score == 3

def test_rand3():
	b = fourtic.Board(file="./boards/rand-3.txt")
	(score, move) = b.negamax(b.player)
	assert score == 0

def test_rand4():
	b = fourtic.Board(file="./boards/rand-4.txt")
	(score, move) = b.negamax(b.player)
	assert score == 3

def test_rand5():
	b = fourtic.Board(file="./boards/rand-5.txt")
	(score, move) = b.negamax(b.player)
	assert score == 0

def test_rand6():
	b = fourtic.Board(file="./boards/rand-6.txt")
	(score, move) = b.negamax(b.player)
	assert score == 0

def test_rand7():
	b = fourtic.Board(file="./boards/rand-7.txt")
	(score, move) = b.negamax(b.player)
	assert score == 1

def test_play2():
	b = fourtic.Board(file="./boards/play-2.txt")
	(score, move) = b.negamax(b.player)
	assert score == 3

def test_play3():
	b = fourtic.Board(file="./boards/play-3.txt")
	(score, move) = b.negamax(b.player)
	assert score == -3

def test_play4():
	b = fourtic.Board(file="./boards/play-4.txt")
	(score, move) = b.negamax(b.player)
	assert score == 3

def test_play5():
	b = fourtic.Board(file="./boards/play-5.txt")
	(score, move) = b.negamax(b.player)
	assert score == 0

def test_play6():
	b = fourtic.Board(file="./boards/play-6.txt")
	(score, move) = b.negamax(b.player)
	assert score == 4

def test_play7():
	b = fourtic.Board(file="./boards/play-7.txt")
	(score, move) = b.negamax(b.player)
	assert score == -2
	
