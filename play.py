from fourtic import Board
from random import randint
import sys

class Play:
	def __init__(self, first=None):
		b = [[".", ".", ".", "."],
			 [".", ".", ".", "."],
			 [".", ".", ".", "."],
			 [".", ".", ".", "."]]
		self.board = Board(b=b)
		if first:
			self.first = first
		else: # 1 = player, 0 = bot
			self.first = randint(0, 1)

	def getMove(self):
		move = input("Select Move (ex. a1, b4): ")
		if move[0] == "a":
			j = 0
		elif move[0] == "b":
			j = 1
		elif move[0] == "c":
			j = 2
		elif move[0] == "d":
			j = 3
		else:
			print("Error: Invalid Input")
			return (-1, -1)
		if len(move) >= 2 and move[1] in ["1", "2", "3", "4"] and \
			self.board.open((int(move[1])-1, j)):
			return (int(move[1])-1, j)
		else:
			print("Error: Invalid Input")
			return (-1, -1)


	def getBoardPos(self, move):
		(i, j) = move
		if j == 0:
			a = "a"
		elif j == 1:
			a = "b"
		elif j == 2:
			a = "c"
		else:
			a = "d"
		return a + str(i+1) 


	def play(self):
		print()
		self.board.print()
		if self.first == 1:
			for m in range(8):
				move = (-1, -1)	
				while move == (-1, -1):
					move = self.getMove()
				self.board.move("X", move)
				self.board.print()
				(score, move) = self.board.negamax("O", depth=4 if m < 4 else None)
				self.board.move("O", move)
				print(f"Bot Move: {self.getBoardPos(move)}")	
				self.board.print()

		else:
			for _ in range(8):
				(score, move) = self.board.negamax("X", depth=4 if m < 4 else None)
				self.board.move("X", move)
				print(f"Bot Move: {self.getBoardPos(move)}")
				self.board.print()
				move = (-1, -1)
				while move == (-1, -1):
					move = self.getMove()
				self.board.move("O", move)
				self.board.print()

		print(f"X: {self.board.score('X')}")
		print(f"O: {self.board.score('O')}")


if __name__ == '__main__':	
	if len(sys.argv) == 2:
		first = int(sys.argv[1])
		play = Play(first=first)
	else:
		play = Play()
	play.play()


