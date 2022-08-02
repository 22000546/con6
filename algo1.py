import random
import utils

def algo1(stone, board, left):
	if left == 2:
		result = find_5stones_open(stone, board, left)
	if len(result) == 0:
		result = find_4stones_open(stone, board, left)
	
	return result

def find_5stones_open(stone, board, left):
	last_ai_move = utils.get_ai_move()
	last_away_move = utils.get_away_move()
	lst = []
	
	if left < 2:
		return lst
 
	if stone == 1:
		stone_list = last_ai_move
	else:
		stone_list = last_away_move

	for (x, y) in stone_list:
  		# 양옆
		for i in range(x-6, x-1):
			if i < 0 or i > 10:
				continue
			if board[y][i] == 0 and board[y][i+1] == 0 and board[y][i+7] == 0 and board[y][i+8] == 0:
				if board[y][i+2] == stone and board[y][i+3] == stone and board[y][i+4] == stone and board[y][i+5] == stone and board[y][i+6] == stone:
					if stone == 1:
						lst.append([(i+1, y), (i+7, y)])
					else:
						lst.append([(i, y), (i+7, y)])
						lst.append([(i+1, y), (i+7, y)])
						lst.append([(i+1, y), (i+8, y)])
		# 위아래
		for i in range(y-5, y-1):
			if i < 0 or i > 10:
				continue
			if board[i][x] == 0 and board[i+1][x] == 0 and board[i+7][x] == 0 and board[i+8][x] == 0:
				if board[i+2][x] == stone and board[i+3][x] == stone and board[i+4][x] == stone and board[i+5][x] == stone and board[i+6][x] == stone:
					if stone == 1:
						lst.append([(x, i+1), (x, i+7)])
					else:
						lst.append([(x, i), (x, i+7)])
						lst.append([(x, i+1), (x, i+7)])
						lst.append([(x, i+1), (x, i+8)])
		# 왼쪽 위 오른쪽 아래 대각선
		for i in range(5):
			if x-6+i < 0 or y-6+i < 0 or x+2+i > 18 or y+2+i > 18:
				continue
			if board[y-6+i][x-6+i] == 0 and board[y-5+i][x-5+i] == 0 and board[y+1+i][x+1+i] == 0 and board[y+2+i][x+2+i] == 0:
				if board[y-4+i][x-4+i] == stone and board[y-3+i][x-3+i] == stone and board[y-2+i][x-2+i] == stone and board[y-1+i][x-1+i] == stone and board[y+i][x+i] == stone:
					if stone == 1:
						lst.append([(x-5+i, y-5+i), (x+1+i, y+1+i)])
					else:
						lst.append([(x-6+i, y-6+i), (x+1+i, y+1+i)])
						lst.append([(x-5+i, y-5+i), (x+1+i, y+1+i)])
						lst.append([(x-5+i, y-5+i), (x+2+i, y+2+i)])
		# 오른쪽 위 왼쪽 아래 대각선
		for i in range(4):
			if x-6+i < 0 or y+6+i > 18 or x+2+i > 18 or y-2+i < 0:
				continue
			if board[y+6+i][x-6+i] == 0 and board[y+5+i][x-5+i] == 0 and board[y-1+i][x+1+i] == 0 and board[y-2+i][x+2+i] == 0:
				if board[y+4+i][x-4+i] == stone and board[y+3+i][x-3+i] == stone and board[y+2+i][x-2+i] == stone and board[y+1+i][x-1+i] == stone and board[y-i][x+i] == stone:
					if stone == 1:
						lst.append([(x-5+i, y+5+i), (x+1+i, y-1+i)])
					else:
						lst.append([(x-6+i, y+6+i), (x+1+i, y-1+i)])
						lst.append([(x-5+i, y+5+i), (x+1+i, y-1+i)])
						lst.append([(x-5+i, y+5+i), (x+2+i, y-2+i)])
    
	if len(lst) != 0:
		select = random.randint(0, len(lst)-1)
		lst = lst[select]
  			
	return lst


def find_4stones_open(stone, board, left):
	last_ai_move = utils.get_ai_move()
	last_away_move = utils.get_away_move()
	lst = []
 
	if left < 2:
		return lst
 
	if stone == 1:
		stone_list = last_ai_move
	else:
		stone_list = last_away_move

	for (x, y) in stone_list:
  		# 양옆
		for i in range(x-5, x-1):
			if i < 0 or i > 11:
				continue
			if board[y][i] == 0 and board[y][i+1] == 0 and board[y][i+6] == 0 and board[y][i+7] == 0:
				if board[y][i+2] == stone and board[y][i+3] == stone and board[y][i+4] == stone and board[y][i+5] == stone:
					if stone == 1:
						lst.append([(i+1, y), (i+6, y)])
					else:
						lst.append([(i, y), (i+6, y)])
						lst.append([(i+1, y), (i+6, y)])
						lst.append([(i+1, y), (i+7, y)])
		# 위아래
		for i in range(y-5, y-1):
			if i < 0 or i > 11:
				continue
			if board[i][x] == 0 and board[i+1][x] == 0 and board[i+6][x] == 0 and board[i+7][x] == 0:
				if board[i+2][x] == stone and board[i+3][x] == stone and board[i+4][x] == stone and board[i+5][x] == stone:
					if stone == 1:
						lst.append([(x, i+1), (x, i+6)])
					else:
						lst.append([(x, i), (x, i+6)])
						lst.append([(x, i+1), (x, i+6)])
						lst.append([(x, i+1), (x, i+7)])
		# 왼쪽 위 오른쪽 아래 대각선
		for i in range(4):
			if x-5+i < 0 or y-5+i < 0 or x+2+i > 18 or y+2+i > 18:
				continue
			if board[y-5+i][x-5+i] == 0 and board[y-4+i][x-4+i] == 0 and board[y+1+i][x+1+i] == 0 and board[y+2+i][x+2+i] == 0:
				if board[y-3+i][x-3+i] == stone and board[y-2+i][x-2+i] == stone and board[y-1+i][x-1+i] == stone and board[y+i][x+i] == stone:
					if stone == 1:
						lst.append([(x-4+i, y-4+i), (x+1+i, y+1+i)])
					else:
						lst.append([(x-5+i, y-5+i), (x+1+i, y+1+i)])
						lst.append([(x-4+i, y-4+i), (x+1+i, y+1+i)])
						lst.append([(x-4+i, y-4+i), (x+2+i, y+2+i)])
		# 오른쪽 위 왼쪽 아래 대각선
		for i in range(4):
			if x-5+i < 0 or y+5+i > 18 or x+2+i > 18 or y-2+i < 0:
				continue
			if board[y+5+i][x-5+i] == 0 and board[y+4+i][x-4+i] == 0 and board[y-1+i][x+1+i] == 0 and board[y-2+i][x+2+i] == 0:
				if board[y+3+i][x-3+i] == stone and board[y+2+i][x-2+i] == stone and board[y+1+i][x-1+i] == stone and board[y-i][x+i] == stone:
					if stone == 1:
						lst.append([(x-4+i, y+4+i), (x+1+i, y-1+i)])
					else:
						lst.append([(x-5+i, y+5+i), (x+1+i, y-1+i)])
						lst.append([(x-4+i, y+4+i), (x+1+i, y-1+i)])
						lst.append([(x-4+i, y+4+i), (x+2+i, y-2+i)])
    
	if len(lst) != 0:
		select = random.randint(0, len(lst)-1)
		lst = lst[select]
					
	return lst