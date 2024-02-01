#!/usr/bin/python3

import sys
from itertools import chain

class Board():
	def __init__(self, file=None, b=None):
		if file:
			self.board = self.makeBoard(file)
		elif b:
			self.board = b
		else:
			print("Error: No board state provided", file=sys.stderr)
			print("Usage: python3 fourtic.py <file>", file=sys.stderr)
			exit(-1)

		(self.player, self.availMoves) = self.evalInitState()

	def negamax(self, player, depth=None):
		moves = self.moves()
		score = float("-inf")
		move = (0, 0)

		if not moves or (depth != None and depth == 0):
			return (self.score(player) - self.score("X" if player == "O" else "O"), None)

		for move in moves:
			(i, j) = move
			self.board[i][j] = player # do
			(s, m) = self.negamax("X" if player == "O" else "O", \
				depth=None if not depth else depth-1)
			if -s > score:
				score = -s
				move = (i, j)

			self.board[i][j] = "." # undo
			
		return (score, move)
		
	def moves(self):
		playable = []
		for i in range(4):
			for j in range(4):
				if self.board[i][j] == ".":
					playable.append((i, j))
		return playable

	def makeBoard(self, file):
		board = []
		with open(file, "r") as f:
			for row in f:
				chars = []
				for char in range(4):
					chars.append(row[char])
				board.append(chars)
		print(board)
		return board

	def stringify(self):
		flatten = list(chain.from_iterable(self.board))
		return ''.join(str(t) for t in flatten)

	def score(self, player):
		score = 0
		for i in range(4):
			for j in range(4):
				if self.board[i][j] == player:
					# edge of board
					if i == 0 or i == 3 or j == 0 or j == 3:
						score += 1
					# check 3/4 in a row
					right = self.inARow("r", player, (i,j))
					ddiag = self.inARow("rd", player, (i,j))
					udiag = self.inARow("ru", player, (i,j))
					down = self.inARow("d", player, (i,j))
					if right:
						score += 3
					if ddiag:
						score += 3
					if udiag:
						score += 3
					if down:
						score += 3
					
		return score

	def inARow(self, direction, player, startPos):
		(i, j) = startPos

		if direction == "r" and j <= 1:
			if self.board[i][j+1] == player and self.board[i][j+2] == player:
				return True
		elif direction == "rd" and i <= 1 and j <= 1:
			if self.board[i+1][j+1] == player and self.board[i+2][j+2] == player:
				return True
		elif direction == "ru" and i >= 2 and j <= 1:
			if self.board[i-1][j+1] == player and self.board[i-2][j+2] == player:
				return True
		elif direction == "d" and i <= 1:
			if self.board[i+1][j] == player and self.board[i+2][j] == player:
				return True
		else:
			return False

		return False

	def evalInitState(self):
		x = 0
		o = 0
		for row in self.board:
			for piece in row:
				if piece == "X":
					x += 1
				if piece == "O":
					o += 1
		return ("X" if x == o else "O", 16-(x+o))

	def print(self):
		for i in range(4):
			print(i + 1, " ", *self.board[i], sep="")
		print("  abcd")
		print()

	def move(self, player, place):
		(i, j) = place
		self.board[i][j] = player

	def open(self, move):
		(i, j) = move
		if self.board[i][j] == ".":
			return True
		return False
		
if __name__ == '__main__':
	if len(sys.argv) >= 2:
		b = Board(file=sys.argv[1])
	else:
		b = Board()
	(score, move) = b.negamax(b.player)
	print(b.player, score)
