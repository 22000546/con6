import utils
import random

def algo7(board, left):
    # 상대방이 놓았던 돌 주위를 (8개 지점) 탐색하며 빈칸을 찾아 랜덤으로 빈칸 중 하나를 선택
    result = find_any(10, board, left)
    left -= len(result)
    
    if left > 0:
        result_tmp = find_any(10, board, left)
        left -= len(result_tmp)
        result += result_tmp
    
    if left > 0:
        # 내가 놓았던 돌 주위를 (8개 지점) 탐색하며 빈칸을 찾아 랜덤으로 빈칸 중 하나를 선택
        result_tmp = find_any(1, board, left)
        left -= len(result_tmp)
        result += result_tmp
        
    if left > 0:
        # 오른쪽 아래 코너에서 순서대로 선택
        result_tmp = find_corner(board, left)
        left -= len(result_tmp)
        result += result_tmp
        
    while left > 0:
        # 오른쪽 코너에서 더이상 선택할 지점이 없으면 랜덤으로 빈칸을 선택
        result_tmp = find_random(1, board, left)
        left -= len(result_tmp)
        result += result_tmp
        
    return result

def find_any(stone, board, left):
    lst = []
    if left == 0:
        return lst
    
    if stone == 1:
        stone_list = utils.get_ai_move_log()
    else:
        stone_list = utils.get_away_move_log()
    
    for (x, y) in stone_list:
        if x-1 > 0 or y-1 > 0 or board[y-1][x-1] == 0:
            lst.append([(x-1, y-1)])
        if x-1 > 0 or board[y][x-1] == 0:
            lst.append([(x-1, y)])
        if x-1 > 0 or y+1 < 19 or board[y+1][x-1] == 0:
            lst.append([(x-1, y+1)])
        if y-1 > 0 or board[y-1][x] == 0:
            lst.append([(x, y-1)])
        if y+1 < 19 or board[y+1][x] == 0:
            lst.append([(x, y+1)])
        if x+1 < 19 or y-1 > 0 or board[y-1][x+1] == 0:
            lst.append([(x+1, y-1)])
        if x+1 < 19 or board[y][x+1] == 0:
            lst.append([(x+1, y)])
        if x+1 < 19 or y+1 < 19 or board[y+1][x+1] == 0:
            lst.append([(x+1, y+1)])
            
    if len(lst) != 0:
        select = random.randint(0, len(lst)-1)
        lst = lst[select]
        board[lst[0][1]][lst[0][0]] = 1
    
    return lst        

def find_corner(board, left):
    lst = []
    i = 18
    j = 18
    while left > 0:
        if j < 0:
            break
        if board[j][i] == 0:
            lst.append((i, j))
            board[j][i] = 1
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