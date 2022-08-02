import random
import algo1
import utils

def algo2(stone, board, left):
	result = algo1.find_5stones_open(stone, board, left)
	left -= len(result)
	if left == 2:
		result = algo1.find_4stones_open(stone, board, left)
		left -= len(result)
  
	while left > 0:
		result_tmp = find_5stones_close(stone, board, left)
		if len(result_tmp) == 0:
			result_tmp = find_4stones_close(stone, board, left)
			if len(result_tmp) == 0:
				break
		result += result_tmp
		left -= len(result_tmp)
  
	return result
  
def find_5stones_close(stone, board, left):
    last_ai_move = utils.get_ai_move()
    last_away_move = utils.get_away_move()
    lst = []
    
    if left == 0:
        return lst
    
    if stone == 1:
        stone_list = last_ai_move
    else:
        stone_list = last_away_move
        
    for (x, y) in stone_list:
        # 양 옆
        for i in range(x-5, x+1):
            if i < 0 or i > 13:
                continue
            sum = board[y][i] + board[y][i+1] + board[y][i+2] + board[y][i+3] + board[y][i+4] + board[y][i+5]
            if sum == 5 * stone:
                for j in range(6):
                    if board[y][i+j] == 0:
                        lst.append([(i+j, y)])          
        # 위아래
        for i in range(y-5, y+1):
            if i < 0 or i > 13:
                continue
            sum = board[i][x] + board[i+1][x] + board[i+2][x] + board[i+3][x] + board[i+4][x] + board[i+5][x]
            if sum == 5 * stone:
                for j in range(6):
                    if board[i+j][x] == 0:
                        lst.append([(x, i+j)])
        # 왼쪽 위 오른쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y-5+i < 0 or x+i > 18 or y+i > 18:
                continue
            sum = board[y-5+i][x-5+i] + board[y-4+i][x-4+i] + board[y-3+i][x-3+i] + board[y-2+i][x-2+i] + board[y-1+i][x-1+i] + board[y+i][x+i]
            if sum == 5 * stone:
                for j in range(6):
                    if board[y-j+i][x-j+i] == 0:
                        lst.append([(x-j+i, y-j+i)])
        # 오른쪽 위 왼쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y+5-i > 18 or x+i > 18 or y-i < 0:
                continue
            sum = board[y+5-i][x-5+i] + board[y+4-i][x-4+i] + board[y+3-i][x-3+i] + board[y+2-i][x-2+i] + board[y+1-i][x-1+i] + board[y-i][x+i]
            if sum == 5 * stone:
                for j in range(6):
                    if board[y+j-i][x-j+i] == 0:
                        lst.append([(x-j+i, y+j-i)])
       
    if len(lst) != 0:
        select = random.randint(0, len(lst)-1)
        lst = lst[select]
        board[lst[0][1]][lst[0][0]] = 1
        
    return lst
				
    
    

def find_4stones_close(stone, board, left):
    last_ai_move = utils.get_ai_move()
    last_away_move = utils.get_away_move()
    lst = []
    
    if left == 0:
        return lst
    
    if stone == 1:
        stone_list = last_ai_move
    else:
        stone_list = last_away_move
        
    for (x, y) in stone_list:
        # 양 옆
        for i in range(x-5, x+1):
            if i < 0 or i > 13:
                continue
            sum = board[y][i] + board[y][i+1] + board[y][i+2] + board[y][i+3] + board[y][i+4] + board[y][i+5]
            if sum == 4 * stone:
                for j in range(6):
                    if board[y][i+j] == 0:
                        lst.append([(i+j, y)])          
        # 위아래
        for i in range(y-5, y+1):
            if i < 0 or i > 13:
                continue
            sum = board[i][x] + board[i+1][x] + board[i+2][x] + board[i+3][x] + board[i+4][x] + board[i+5][x]
            if sum == 4 * stone:
                for j in range(6):
                    if board[i+j][x] == 0:
                        lst.append([(x, i+j)])
        # 왼쪽 위 오른쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y-5+i < 0 or x+i > 18 or y+i > 18:
                continue
            sum = board[y-5+i][x-5+i] + board[y-4+i][x-4+i] + board[y-3+i][x-3+i] + board[y-2+i][x-2+i] + board[y-1+i][x-1+i] + board[y+i][x+i]
            if sum == 4 * stone:
                for j in range(6):
                    if board[y-j+i][x-j+i] == 0:
                        lst.append([(x-j+i, y-j+i)])
        # 오른쪽 위 왼쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y+5-i > 18 or x+i > 18 or y-i < 0:
                continue
            sum = board[y+5-i][x-5+i] + board[y+4-i][x-4+i] + board[y+3-i][x-3+i] + board[y+2-i][x-2+i] + board[y+1-i][x-1+i] + board[y-i][x+i]
            if sum == 4 * stone:
                for j in range(6):
                    if board[y+j-i][x-j+i] == 0:
                        lst.append([(x-j+i, y+j-i)])
       
    if len(lst) != 0:
        select = random.randint(0, len(lst)-1)
        lst = lst[select]
        board[lst[0][1]][lst[0][0]] = 1
        
    return lst