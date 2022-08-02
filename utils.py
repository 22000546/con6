'''

'''
from regex import B
from CONNSIX import connsix
import algo1
import algo2
import algo7
import algo4
import attack2

last_ai_move = None #[(x,y)] list
last_away_move = None

def set_ai_move(ai_move):
	global last_ai_move
	last_ai_move = ai_move

def set_away_move(away_move):
	global last_away_move
	last_away_move = coor_to_num(away_move)
 
def get_ai_move():
	global last_ai_move
	return last_ai_move

def get_away_move():
	global last_away_move
	return last_away_move    

def make_move(board):
	global last_ai_move, last_away_move
	left = 2
 
	# 1. 내가 끝낼 수 있는 경우
	result = algo1.algo1(1, board, left)
	if len(result) != 0:
		print("algo1 : ", len(result))
	final_result = result
	left -= len(result)
	# 2. 내가 무조건 막아야 하는 경우
	result = algo2.algo2(10, board, left)
	if len(result) != 0:
		print("algo2 : ", len(result))
	final_result += result
	left -= len(result)
	# 3. 상대가 돌 2개를 사용하도록 공격하는 경우
	result = attack2.attack_2(board, last_ai_move, left)
	if len(result) != 0:
		print("algo3 : ", len(result))
	final_result += result
	left -= len(result)
	# 4. 상대가 돌 1개를 사용하도록 공격하는 경우
	result = algo4.algo4(left, 1, board)
	final_result += result
	left -= len(result)

	# 5. 방어하는 경우
	# 6. 아무것도 할 게 없는 경우 (코너 -> 랜덤)
	# result = algo7.find_corner(board, left)
	# final_result += result
	# left -= len(result)
	result = algo7.find_random(1, board, left)
	if(len(result) != 0):
		print("algo7 : ", len(result))
	final_result += result
	left -= len(result)
 
	last_ai_move = final_result
	return num_to_coor(final_result)

def num_to_coor(lst):
	if lst is None:
		return None

	result = ""
	
	for (x,y) in lst:
		if x > 7 :
			x += 1
		row = chr(x+65)
		col = 19 - y
		result = result + ":" + row + str(col)
	result = result[1:]      
	return result 

def coor_to_num(lst):
	result = []
	stones = lst.split(":")
	
	for i in stones:
		x = ord(i[0])-65
		if x > 8:
			x -= 1
		result.append((x, 19-int(i[1:])))
	
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
                board[y][x] = 100
            elif ret == ai_home[0]:
                board[y][x] = 1 
            else:    
                board[y][x] = 10
    return board