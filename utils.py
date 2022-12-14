'''

'''
from CONNSIX import connsix
import first
import algo1
import algo2
import algo6
import algo7
import algo4
import attack2

last_ai_move = None #[(x,y)] list
last_away_move = None
ai_move_log = None
away_move_log = []
isBlack = True

def set_ai_move(ai_move):
	global last_ai_move, ai_move_log
	last_ai_move = ai_move
	ai_move_log = last_ai_move

def set_away_move(away_move):
	global last_away_move, away_move_log
	last_away_move = coor_to_num(away_move)
	away_move_log = last_away_move + away_move_log
 
def get_ai_move():
	global last_ai_move
	return last_ai_move

def get_away_move():
	global last_away_move
	return last_away_move

def get_ai_move_log():
    global ai_move_log
    return ai_move_log    

def get_away_move_log():
    global away_move_log
    return away_move_log

def make_move(board):
	global last_ai_move, last_away_move, ai_move_log, isBlack
	left = 2
  
	if last_ai_move == None:
		isBlack = False
		final_result = first.find_first(board)
		ai_move_log = final_result
		last_ai_move = final_result
		return num_to_coor(final_result)
 
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
	result = attack2.attack_2(board, ai_move_log, left)
	if len(result) != 0:
		print("algo3 : ", len(result))
	final_result += result
	left -= len(result)
	# 4. 상대가 돌 1개를 사용하도록 공격하는 경우
	result = algo4.algo4(left, 1, board)
	if len(result) != 0:
		print("algo4 : ", len(result))
	final_result += result
	left -= len(result)
	# 5. 방어하는 경우
	result = algo6.algo6(board, left)
	if len(result) != 0:
		print("algo6 : ", len(result))
	final_result += result
	left -= len(result)
	# 6. 아무것도 할 게 없는 경우
	result = algo7.algo7(board, left)
	if(len(result) != 0):
		print("algo7 : ", len(result))
	final_result += result
	left -= len(result)
 
	ai_move_log = final_result + ai_move_log
	# ai_move_log = last_ai_move + final_result
	last_ai_move = final_result
	print(final_result)
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

def get_max_open_point(stone, board, points):
    global isBlack
    # points = [(x,y), (x,y), ...]
    # print("point", points)
    
    max_open = -1
    for (x, y) in points:
        point = [(x, y)]
        board[y][x] = 1
        # print("point", point)
        close5 = len(algo1.find_5stones_close(1, board, 2, point, 1))
        close4 = len(algo2.find_4stones_close(1, board, 2, point, 1))
        open2 = len(attack2.open2(1, board, point))
        open3 = len(attack2.open3(1, board, point))
        close3 = len(algo4.find_3stones_close(1, board, point))
        board[y][x] = 0
        defense1 = len(attack2.open2(10, board, point)) # 상대방 열린 2 막기 
        defense2 = len(attack2.open3(10, board, point)) # 상대방 열린 3 막기 
        defense3 = len(attack2.open2(5, board, point)) # 상대방 열린 1 막기 
        if isBlack :
            new_score = open2 + open3 + close3 + close4 + close5 + defense1 + defense2
            new_length = [close5, close4, defense2, defense1, open3, open2, close3, defense3]
        else :
            new_score = open2 + open3 + close3 + close4 + close5
            new_length = [close5, close4, open3, open2, close3, defense2, defense1, defense3] 
        # print("x,y",x,y, "==",new_length)
        if new_score > max_open:
            max_open = new_score
            max_point = point
            max_length = new_length
        elif new_score == max_open:
            if max_length[0] < new_length[0]:
                max_open = new_score
                max_point = point
                max_length = new_length
            elif max_length[0] == new_length[0]:
                if max_length[1] < new_length[1]:
                    max_open = new_score
                    max_point = point
                    max_length = new_length
                elif max_length[1] == new_length[1]:
                    if max_length[2] < new_length[2]:
                        max_open = new_score
                        max_point = point
                        max_length = new_length
                    elif max_length[2] == new_length[2]:
                        if max_length[3] < new_length[3]:
                            max_open = new_score
                            max_point = point
                            max_length = new_length
                        elif max_length[3] == new_length[3]:
                            if max_length[4] < new_length[4]:
                                max_open = new_score
                                max_point = point
                                max_length = new_length
                            elif max_length[4] == new_length[4]:
                                if max_length[5] < new_length[5]:
                                    max_open = new_score
                                    max_point = point
                                    max_length = new_length
                                elif max_length[5] == new_length[5]:
                                    if max_length[6] < new_length[6]:
                                        max_open = new_score
                                        max_point = point
                                        max_length = new_length
                                    elif max_length[6] == new_length[6]:
                                        if max_length[7] < new_length[7]:
                                            max_open = new_score
                                            max_points = point
                                            max_length = new_length
        
    return max_point

def get_max_open_points(stone, board, points):
    # points = [ [(x,y), (x,y)], [(x,y), (x,y)], ...]
    # print("point", points)
        
    max_open = -1
    for point in points:
        [(x1, y1), (x2, y2)] = point
        board[y1][x1] = 1
        board[y2][x2] = 1
        close5 = len(algo1.find_5stones_close(1, board, 2, point))
        close4 = len(algo2.find_4stones_close(1, board, 2, point))
        open2 = len(attack2.open2(1, board, point))
        open3 = len(attack2.open3(1, board, point))
        close3 = len(algo4.find_3stones_close(1, board, point))
        board[y1][x1] = 0
        board[y2][x2] = 0
        defense1 = len(attack2.open2(10, board, point))
        defense2 = len(attack2.open3(10, board, point))
        defense3 = len(attack2.open2(5, board, point))
        if isBlack :
            new_score = open2 + open3 + close3 + close4 + close5 + defense1 + defense2
            new_length = [close5, close4, defense2, defense1, open3, open2, close3, defense3]
        else :
            new_score = open2 + open3 + close3 + close4 + close5
            new_length = [close5, close4, open3, open2, close3, defense2, defense1, defense3] 
        # print("point",point, "==", new_length)
        if new_score > max_open:
            max_open = new_score
            max_points = point
            max_length = new_length
        elif new_score == max_open:
            if max_length[0] < new_length[0]:
                max_open = new_score
                max_points = point
                max_length = new_length
            elif max_length[0] == new_length[0]:
                if max_length[1] < new_length[1]:
                    max_open = new_score
                    max_points = point
                    max_length = new_length
                elif max_length[1] == new_length[1]:
                    if max_length[2] < new_length[2]:
                        max_open = new_score
                        max_points = point
                        max_length = new_length
                    elif max_length[2] == new_length[2]:
                        if max_length[3] < new_length[3]:
                            max_open = new_score
                            max_points = point
                            max_length = new_length
                        elif max_length[3] == new_length[3]:
                            if max_length[4] < new_length[4]:
                                max_open = new_score
                                max_points = point
                                max_length = new_length
                            elif max_length[4] == new_length[4]:
                                if max_length[5] < new_length[5]:
                                    max_open = new_score
                                    max_points = point
                                    max_length = new_length
                                elif max_length[5] == new_length[5]:
                                    if max_length[6] < new_length[6]:
                                        max_open = new_score
                                        max_points = point
                                        max_length = new_length
                                    elif max_length[6] == new_length[6]:
                                        if max_length[7] < new_length[7]:
                                            max_open = new_score
                                            max_points = point
                                            max_length = new_length
        
    return max_points

def get_max_open_set_points(stone, board, sets):        
    max_lst = []
    for set in sets:
        point_lst = set
        tmp = get_max_open_points(1, board, point_lst)
        max_lst.append(tmp)
        
    result = get_max_open_points(1, board, max_lst)
    return result
        