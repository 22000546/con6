'''

'''
from CONNSIX import connsix
import ai 
import random 

def make_move(board):
	# 1. 내가 끝낼 수 있는 경우
	# 2. 내가 무조건 막아야 하는 경우
	# 3. 상대가 돌 2개를 사용하도록 공격하는 경우
	# 4. 상대가 돌 1개를 사용하도록 공격하는 경우
	# 5. 아무것도 할 게 없는 경우 (랜덤)
	result = find_random(board)
	return num_to_coor(result)

def num_to_coor(lst):
	result = ""
	
	for (x,y) in lst:
		if x > 7 :
			x += 1
		row = chr(x+65)
		col = 19 - y
		result = result + ":" + row + str(col)
	result = result[1:]      
	return result 

def get_board(ai_home):
    # A~T (I 제외)
    # 1~19
    board = [[0 for i in range(19)] for j in range(19)]

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

    for i in alphabets:
        for j in range(1,20):
            ret = connsix.get_stone_at(i+str(j))
            x = ord(i) - 97
            y = 19 - j
            if x > 8:
                x = x - 1
            if ret == 'N':
                continue
            elif ret == 'E':
                board[y][x] = 0 
            elif ret == 'R':
                board[y][x] = 3 
            elif ret == ai_home[0]:
                board[y][x] = 1 
            else:    
                board[y][x] = -1 
    return board 

def find_random(board):
	lst = []
	x1 = random.randint(0, 18)
	y1 = random.randint(0, 18)
	while board[y1][x1] != 0:
		x1 = random.randint(0, 18)
		y1 = random.randint(0, 18)
	lst.append((x1, y1))

	x2 = random.randint(0, 18)
	y2 = random.randint(0, 18)
	while board[y2][x2] != 0:
		x2 = random.randint(0, 18)
		y2 = random.randint(0, 18)
	lst.append((x2, y2))
	return lst