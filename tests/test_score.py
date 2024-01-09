import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fourtic

def test_right():
	b = fourtic.Board(b=["XXXO", "OOOO", "XOXX", "OXOX"])
	assert b.score("X") == 10

def test_ddiag():
	b = fourtic.Board(b=["XOXX", "OXOO", "OOXX", "XXOO"])
	assert b.score("X") == 9

def test_udiag():
	b = fourtic.Board(b=["XOXX", "OXOO", "XOOX", "OXOX"])
	assert b.score("X") == 10

def test_down():
	b = fourtic.Board(b=["XOXX", "XOOO", "XOXX", "OXOO"])
	assert b.score("X") == 10

def test_4row():
	b = fourtic.Board(b=["XXXX", "OOOO", "OXOO", "OOOO"])
	assert b.score("X") == 10

def test_4rowx2():
	b = fourtic.Board(b=["XXXX", "OOXO", "OXOO", "XOOO"])
	assert b.score("X") == 17 
	assert b.score("O") == 19

def test_rand1():
	b = fourtic.Board(b=["OOOX", "XXOO", "XOXX", "OXOX"])
	assert b.score("X") == 9
	
def test_rand2():
	b = fourtic.Board(b=["XXOX", "OXOO", "OXOO", "XXXO"])
	assert b.score("X") == 15
	assert b.score("O") == 12 

def test_ex():
	b = fourtic.Board(b=["OOXO", "XXXX", "OXOX", "OOXO"])
	assert b.score("X") == 14
	assert b.score("O") == 7
