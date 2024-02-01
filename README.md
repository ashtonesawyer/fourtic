# Fourtic
Ashton Sawyer

Fourtic is a 4x4 Tic-Tac-Tor variant designed by Bart Massey. 

## Playing
As in Tic-Tac-Toe, `X` goes first and then players take turns.

### Scoring
3-in-a-row counts for 3 points (4-in-a-row counts for 6 as
there are 2 sets of 3-in-a-row within it). Each tile on the outside of the board 
counts for another point. Each game is played to completion and then scored. The
player with the highest score wins.

## Format
Each board is represented in ASCII with `.` counting for open spaces

## Description
The main file `fourtic.py` solves a given board state with a full negamax.
I referenced [Wikipedia](https://en.wikipedia.org/wiki/Negamax) 
some for their algorithm descriptions. Even
the longest puzzles take less than .3 seconds to complete. 

### Negamax and Playing
`fourtic.py` has the main negamax algorithm and `play.py` is so that a human can play against
the computer. When playing a human, the negamax has depth 4 until the 4th round when it switches
to a full search. 

### Solving - unfinished
`solve.py` uses retrograde analysis to strongly solve fourtic. The turn table is represented
by a sqlite3 database in `states.db`. The `solution` table in this database stores the 
board state, the score where `score = scoreX - scoreO`, and (where applicable) the best move
to be played. In its current state is runs slowly and generates an incorrect answer, though it 
does get through all of the states. Rather than using the database, it currently dumps the output
into a JSON file for faster storage.


### Example Game
```
....  X...  XX..  XX..  XX.X  XXXX  XXXX  XXXX  XXXX
....  ....  ....  ....  ....  ....  ....  X..O  XXOO
....  ....  ....  ....  ...O  ..OO  XOOO  XOOO  XOOO
....  ...O  ..OO  OXOO  OXOO  OXOO  OXOO  OXOO  OXOO

Final Score:
	X (player) : 19
	O (bot)    : 17
```


## Use
```
	python3 fourtic.py <file>  -- negamax

	python3 play.py [0 | 1]    -- playing
		- 0 
		  Bot goes first

		- 1
		  Player goes first
		- Blank
		  Who goes first is randomly chosen

	python3 solve.py           -- solving
```

## Testing
Automated unit tests were written with pytest
