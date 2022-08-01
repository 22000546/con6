import random

def find_corner(board, left):
    lst = []
    i = 18
    j = 18
    while left > 0:
        if board[j][i] == 0:
            lst.append((i, j))
            left -= 1
        j -= 1
            
    return lst

def find_random(stone, board, left):
	lst = []
	
	while left > 0:
		x = random.randint(0, 18)
		y = random.randint(0, 18)
		if board[y][x] == 0:
			lst.append((x, y))
			board[y][x] = stone
			left -= 1

	return lst