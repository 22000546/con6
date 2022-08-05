import utils
import algo1

def algo2(stone, board, left):
	result = find_5stones_open(stone, board, left) # returns two stones
	left -= len(result)
 
	while left > 0:
		result_tmp = algo1.find_5stones_close(stone, board, left) # returns one stone
		result += result_tmp
		left -= len(result_tmp)
		if len(result_tmp) == 0:
			break
		else:
			board[result_tmp[0][1]][result_tmp[0][0]] = 1
			print("5 close")

	if left == 2:
		result = find_4stones_open(stone, board, left) # returns two stones
		left -= len(result)
  
	while left > 0:
		result_tmp = find_4stones_semi_open(stone, board, left) # returns one stone
		result += result_tmp
		left -= len(result_tmp)
		if len(result_tmp) == 0:
			break
		else:
			board[result_tmp[0][1]][result_tmp[0][0]] = 1
			print("semi open")
   
	while left > 0:
		result_tmp = find_4stones_semi_close(stone, board, left) # returns one stone
		result += result_tmp
		left -= len(result_tmp)
		if len(result_tmp) == 0:
			break
		else:
			board[result_tmp[0][1]][result_tmp[0][0]] = 1
			print("semi close")

	while left > 0:
		result_tmp = find_4stones_close(stone, board, left) # returns one stone
		result += result_tmp
		left -= len(result_tmp)
		if len(result_tmp) == 0:
			break
		else:
			board[result_tmp[0][1]][result_tmp[0][0]] = 1
			print("4 close")
  
	return result

def find_5stones_open(stone, board, left):
	ai_move_log = utils.get_ai_move_log()
	away_move_log = utils.get_away_move_log()
	lst = []
	
	if left < 2:
		return lst
 
	if stone == 1:
		stone_list = ai_move_log
	else:
		stone_list = away_move_log

	for (x, y) in stone_list:
  		# 양옆
		for i in range(x-6, x-1):
			if i < 0 or i > 10:
				continue
			if board[y][i] == 0 and board[y][i+1] == 0 and board[y][i+7] == 0 and board[y][i+8] == 0:
				if board[y][i+2] == stone and board[y][i+3] == stone and board[y][i+4] == stone and board[y][i+5] == stone and board[y][i+6] == stone:
					lst.append([(i+1, y), (i+7, y)])
		# 위아래
		for i in range(y-5, y-1):
			if i < 0 or i > 10:
				continue
			if board[i][x] == 0 and board[i+1][x] == 0 and board[i+7][x] == 0 and board[i+8][x] == 0:
				if board[i+2][x] == stone and board[i+3][x] == stone and board[i+4][x] == stone and board[i+5][x] == stone and board[i+6][x] == stone:
					lst.append([(x, i+1), (x, i+7)])
		# 왼쪽 위 오른쪽 아래 대각선
		for i in range(5):
			if x-6+i < 0 or y-6+i < 0 or x+2+i > 18 or y+2+i > 18:
				continue
			if board[y-6+i][x-6+i] == 0 and board[y-5+i][x-5+i] == 0 and board[y+1+i][x+1+i] == 0 and board[y+2+i][x+2+i] == 0:
				if board[y-4+i][x-4+i] == stone and board[y-3+i][x-3+i] == stone and board[y-2+i][x-2+i] == stone and board[y-1+i][x-1+i] == stone and board[y+i][x+i] == stone:
					lst.append([(x-5+i, y-5+i), (x+1+i, y+1+i)])
		# 오른쪽 위 왼쪽 아래 대각선
		for i in range(5):
			if x-6+i < 0 or y+6-i > 18 or x+2+i > 18 or y-2-i < 0:
				continue
			if board[y+6-i][x-6+i] == 0 and board[y+5-i][x-5+i] == 0 and board[y-1-i][x+1+i] == 0 and board[y-2-i][x+2+i] == 0:
				if board[y+4-i][x-4+i] == stone and board[y+3-i][x-3+i] == stone and board[y+2-i][x-2+i] == stone and board[y+1-i][x-1+i] == stone and board[y-i][x+i] == stone:
					lst.append([(x-5+i, y+5-i), (x+1+i, y-1-i)])
    
	if len(lst) != 0:
		lst = utils.get_max_open_points(1, board, lst)
  			
	return lst

def find_4stones_open(stone, board, left):
	away_move_log = utils.get_away_move_log()
	ai_move_log = utils.get_ai_move_log()
	lst = []
 
	if left < 2:
		return lst
 
	if stone == 1:
		stone_list = ai_move_log
	else:
		stone_list = away_move_log

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
			if board[y+5-i][x-5+i] == 0 and board[y+4-i][x-4+i] == 0 and board[y-1-i][x+1+i] == 0 and board[y-2-i][x+2+i] == 0:
				if board[y+3-i][x-3+i] == stone and board[y+2-i][x-2+i] == stone and board[y+1-i][x-1+i] == stone and board[y-i][x+i] == stone:
					if stone == 1:
						lst.append([(x-4+i, y+4-i), (x+1+i, y-1-i)])
					else:
						lst.append([(x-5+i, y+5-i), (x+1+i, y-1-i)])
						lst.append([(x-4+i, y+4-i), (x+1+i, y-1-i)])
						lst.append([(x-4+i, y+4-i), (x+2+i, y-2-i)])
    
	if len(lst) != 0:
		lst = utils.get_max_open_points(1, board, lst)
	
	return lst

def find_4stones_semi_open(stone, board, left):
    ai_move_log = utils.get_ai_move_log()
    away_move_log = utils.get_away_move_log()
    lst = []
    
    if left == 0:
        return lst
    
    if stone == 1:
        stone_list = ai_move_log
    else:
        stone_list = away_move_log
        
    for (x, y) in stone_list:
		# 양옆
        for i in range(x-4, x):
            if i < 0 or i > 13:
                continue
            if board[y][i] == 0 and board[y][i+1] == stone and board[y][i+2] == stone and board[y][i+3] == stone and board[y][i+4] == stone and board[y][i+5] == 0:
                if i-1 < 0 or board[y][i-1] != 0: # 왼쪽 막힘
                    lst.append((i+5, y))
                elif i+6 > 18 or board[y][i+6] != 0: # 오른쪽 막힘
                    lst.append((i, y))
        # 위아래
        for i in range(y-4, y):
            if i < 0 or i > 13:
                continue
            if board[i][x] == 0 and board[i+1][x] == stone and board[i+2][x] == stone and board[i+3][x] == stone and board[i+4][x] == stone and board[i+5][x] == 0:
                if i-1 < 0 or board[i-1][x] != 0: # 왼쪽 막힘
                    lst.append((x, i+5))
                elif i+6 > 18 or board[i+6][x] != 0: # 오른쪽 막힘
                    lst.append((x, i))
        # 왼쪽 위 오른쪽 아래 대각선
        for i in range(4):
            if x-4+i < 0 or y-4+i < 0 or x+1+i > 18 or y+1+i > 18:
                continue
            if board[y-4+i][x-4+i] == 0 and board[y-3+i][x-3+i] == stone and board[y-2+i][x-2+i] == stone and board[y-1+i][x-1+i] == stone and board[y+i][x+i] == stone and board[y+1+i][x+1+i] == 0:
                if x-5+i < 0 or y-5+i < 0 or board[y-5+i][x-5+i] != 0: # 왼쪽 막힘
                    lst.append((x+1+i, y+1+i))
                elif x+2+i > 18 or y+2+i > 18 or board[y+2+i][x+2+i] != 0: # 오른쪽 막힘
                    lst.append((x-4+i, y-4+i))
        # 오른쪽 위 왼쪽 아래 대각선
        for i in range(4):
            if x-4+i < 0 or y+4-i > 18 or x+1+i > 18 or y-1-i < 0:
                continue
            if board[y+4-i][x-4+i] == 0 and board[y+3-i][x-3+i] == stone and board[y+2-i][x-2+i] == stone and board[y+1-i][x-1+i] == stone and board[y-i][x+i] == stone and board[y-1-i][x+1+i] == 0:
                if x-5+i < 0 or y+5-i > 18 or board[y+5-i][x-5+i] != 0: # 왼쪽 막힘
                    lst.append((x+1+i, y-1-i))
                elif x+2+i > 18 or y-2-i < 0 or board[y-2-i][x+2+i] != 0: # 오른쪽 막힘
                    lst.append((x-4+i, y+4-i))
        
    if len(lst) != 0:
        lst = utils.get_max_open_point(1, board, lst)
    
    return lst

def find_4stones_semi_close(stone, board, left):
    ai_move_log = utils.get_ai_move_log()
    away_move_log = utils.get_away_move_log()
    lst = []
    
    if left == 0:
        return lst
    
    if stone == 1:
        stone_list = ai_move_log
    else:
        stone_list = away_move_log
        
    for (x, y) in stone_list:
        for i in range(5):
            # 양옆
            if x-5+i < 0 or x+1+i > 18:
                continue
            if board[y][x-5+i] == 0 and board[y][x+1+i] == 0:
                # _XX_XX_
                if board[y][x-4+i] == stone and board[y][x-3+i] == stone and board[y][x-2+i] == 0 and board[y][x-1+i] == stone and board[y][x+i] == stone:
                    lst.append((x-2+i, y))
				# _X_XXX_
                elif board[y][x-4+i] == stone and board[y][x-3+i] == 0 and board[y][x-2+i] == stone and board[y][x-1+i] == stone and board[y][x+i] == stone:
                    lst.append((x-3+i, y))
                # _XXX_X_
                elif board[y][x-4+i] == stone and board[y][x-3+i] == stone and board[y][x-2+i] == stone and board[y][x-1+i] == 0 and board[y][x+i] == stone:
                    lst.append((x-1+i, y))
            # 위아래
            if y-5+i < 0 or y+1+i > 18:
                continue
            if board[y-5+i][x] == 0 and board[y+1+i][x] == 0:
                # _XX_XX_
                if board[y-4+i][x] == stone and board[y-3+i][x] == stone and board[y-2+i][x] == 0 and board[y-1+i][x] == stone and board[y+i][x] == stone:
                    lst.append((x, y-2+i))
				# _X_XXX_
                elif board[y-4+i][x] == stone and board[y-3+i][x] == 0 and board[y-2+i][x] == stone and board[y-1+i][x] == stone and board[y+i][x] == stone:
                    lst.append((x, y-3+i))
                # _XXX_X_
                elif board[y-4+i][x] == stone and board[y-3+i][x] == stone and board[y-2+i][x] == stone and board[y-1+i][x] == 0 and board[y+i][x] == stone:
                    lst.append((x, y-1+i))
            # 왼쪽 위 오른쪽 아래 대각선
            if x-5+i < 0 or x+1+i > 18 or y-5+i < 0 or y+1+i > 18:
                continue
            if board[y-5+i][x-5+i] == 0 and board[y+1+i][x+1+i] == 0:
                # _XX_XX_
                if board[y-4+i][x-4+i] == stone and board[y-3+i][x-3+i] == stone and board[y-2+i][x-2+i] == 0 and board[y-1+i][x-1+i] == stone and board[y+i][x+i] == stone:
                    lst.append((x-2+i, y-2+i))
				# _X_XXX_
                elif board[y-4+i][x-4+i] == stone and board[y-3+i][x-3+i] == 0 and board[y-2+i][x-2+i] == stone and board[y-1+i][x-1+i] == stone and board[y+i][x+i] == stone:
                    lst.append((x-3+i, y-3+i))
                # _XXX_X_
                elif board[y-4+i][x-4+i] == stone and board[y-3+i][x-3+i] == stone and board[y-2+i][x-2+i] == stone and board[y-1+i][x-1+i] == 0 and board[y+i][x+i] == stone:
                    lst.append((x-1+i, y-1+i))
            # 오른쪽 위 왼쪽 아래 대각선
            if x-5+i < 0 or x+1+i > 18 or y+5-i > 18 or y-1-i < 0:
                continue
            if board[y+5-i][x-5+i] == 0 and board[y-1-i][x+1+i] == 0:
                # _XX_XX_
                if board[y+4-i][x-4+i] == stone and board[y+3-i][x-3+i] == stone and board[y+2-i][x-2+i] == 0 and board[y+1-i][x-1+i] == stone and board[y-i][x+i] == stone:
                    lst.append((x-2+i, y+2-i))
				# _X_XXX_
                elif board[y+4-i][x-4+i] == stone and board[y+3-i][x-3+i] == 0 and board[y+2-i][x-2+i] == stone and board[y+1-i][x-1+i] == stone and board[y-i][x+i] == stone:
                    lst.append((x-3+i, y+3-i))
                # _XXX_X_
                elif board[y+4-i][x-4+i] == stone and board[y+3-i][x-3+i] == stone and board[y+2-i][x-2+i] == stone and board[y+1-i][x-1+i] == 0 and board[y-i][x+i] == stone:
                    lst.append((x-1+i, y+1-i))
    
    if len(lst) != 0:
        lst = utils.get_max_open_point(1, board, lst)
    
    return lst

def find_4stones_close(stone, board, left, stone_list=None, flag=0):
    ai_move_log = utils.get_ai_move_log()
    away_move_log = utils.get_away_move_log()
    lst = []
    
    if left == 0:
        return lst
    
    if stone_list is None:
        if stone == 1:
            stone_list = ai_move_log
        else:
            stone_list = away_move_log
        
    for (x, y) in stone_list:
        # 양 옆
        for i in range(x-5, x+1):
            if i < 0 or i > 13:
                continue
            sum = board[y][i] + board[y][i+1] + board[y][i+2] + board[y][i+3] + board[y][i+4] + board[y][i+5]
            if sum == 4 * stone:
                for j in range(6):
                    if board[y][i+j] == 0:
                        lst.append((i+j, y))          
        # 위아래
        for i in range(y-5, y+1):
            if i < 0 or i > 13:
                continue
            sum = board[i][x] + board[i+1][x] + board[i+2][x] + board[i+3][x] + board[i+4][x] + board[i+5][x]
            if sum == 4 * stone:
                for j in range(6):
                    if board[i+j][x] == 0:
                        lst.append((x, i+j))
        # 왼쪽 위 오른쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y-5+i < 0 or x+i > 18 or y+i > 18:
                continue
            sum = board[y-5+i][x-5+i] + board[y-4+i][x-4+i] + board[y-3+i][x-3+i] + board[y-2+i][x-2+i] + board[y-1+i][x-1+i] + board[y+i][x+i]
            if sum == 4 * stone:
                for j in range(6):
                    if board[y-j+i][x-j+i] == 0:
                        lst.append((x-j+i, y-j+i))
        # 오른쪽 위 왼쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y+5-i > 18 or x+i > 18 or y-i < 0:
                continue
            sum = board[y+5-i][x-5+i] + board[y+4-i][x-4+i] + board[y+3-i][x-3+i] + board[y+2-i][x-2+i] + board[y+1-i][x-1+i] + board[y-i][x+i]
            if sum == 4 * stone:
                for j in range(6):
                    if board[y+j-i][x-j+i] == 0:
                        lst.append((x-j+i, y+j-i))
       
    if len(lst) != 0:
        if flag == 0:
            lst = utils.get_max_open_point(1, board, lst)
        
    return lst