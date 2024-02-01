#!/usr/bin/python3

import json
import sqlite3 as sql
import threading as td
from itertools import combinations
from fourtic import Board

db = sql.connect("states.db")
cur = db.cursor()

ttable = {} # stored as state: (move, score)

def createDB():
	cur.execute("DROP TABLE solution")
	cur.execute("CREATE TABLE IF NOT EXISTS solution(state TEXT PRIMARY KEY, \
	score INTEGER NOT NULL,	next_move TEXT)")

	# check if table created
	result = cur.execute("SELECT name FROM sqlite_master")
	if result is None:
		print("Error: Unable to create table")
		exit(-1)

def storeDB():
	for state in ttable:
		(move, score) = ttable[state]
		data = ({"state": state, "move": move, "score": score})
		cur.execute("INSERT INTO solution VALUES(:state, :move, :score)")

	db.commit()

def genEndStates():
	"""Auto Generate all possible ending states

	:return Array of states in string form
	"""
	states = []
	spaces = [(0,0), (0,1), (0,2), (0,3), 
			  (1,0), (1,1), (1,2), (1,3),
			  (2,0), (2,1), (2,2), (2,3),
			  (3,0), (3,1), (3,2), (3,3)]
	#put down X's
	selected = list(combinations(spaces, 8))
	for state in selected:
		board = [['', '', '', ''],
				 ['', '', '', ''],
				 ['', '', '', ''],
				 ['', '', '', '']]
		for coord in state:
			(i, j) = coord
			board[i][j] = 'X'
		states.append(board)

	#fill in gaps with O's
	for board in states:
		for i in range(4):
			for j in range(4):
				if board[i][j] != 'X':
					board[i][j] = 'O'
	
	return states

def getMoves(board, player):
	'''Generate all possible moves'''
	moves = []
	for i in range(4):
		for j in range(4):
			if board.board[i][j] == player:
				moves.append((i, j))

	return moves

def retrograde(board, player, move, score, cnt=None):
	'''Perform a full retrograde analysis

	:param board 
	:param player The current player
	:param move The move that the state came from
	'''
	rep = board.stringify()
	
	lock = td.Lock()
	lock.acquire()
	if not lock.locked():
		print("Error: Lock not acquired")
	if rep in ttable:
		(m, s) = ttable[rep]
		if player == 'O':
			if score < s:
				ttable[rep] = (move, score)
			else:
				return
		else:
			if score > s:
				ttable[rep] = (move, score)
			else:
				return
	else:
		ttable[rep] = (move, score)
	lock.release()


	if cnt is not None:
		cnt -= 1
		if cnt == 0:
			return

	moves = getMoves(board, player)
	if not moves:
		return
	
	for move in moves:
		(i, j) = move
		tmp = board.board[i][j]
		board.board[i][j] = '.' # do
		retrograde(board, 'X' if player == 'O' else 'O', (i, j), score, cnt)
		board.board[i][j] = tmp # undo
		
def threadFxn(boards, start):
	"""Wrapper for retrograde() for threads

	:param start: starting index for calling retrograde w/ boards
	"""
	for i in range(start, start + 13):
		if i >= len(boards):
			return

		score = boards[i].score('X') - boards[i].score('O')
		retrograde(boards[i], 'O', None, score)



if __name__ == '__main__':
	states = genEndStates()
	
	boards = []
	for state in states:
		boards.append(Board(b=state))	

	# create threads
	threads = []
	for i in range(0, len(boards), 13):
		threads.append(td.Thread(target=threadFxn, args=(boards, i)))

	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

	# temporary for faster checking
	jsonObj = json.dumps(ttable, indent=2)
	with open("tmp.json", "w") as out:
		out.write(jsonObj)

	#createDB()
	#storeDB()

