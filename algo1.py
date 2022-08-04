import utils

def algo1(stone, board, left):
	if left > 0:
		result = find_5stones_close(stone, board, left)
		if len(result) != 0:
			return result
	if left == 2:
		result = find_4stones_close(stone, board, left)	
	return result

def find_5stones_close(stone, board, left):
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
        # 양 옆
        for i in range(x-5, x+1):
            if i < 0 or i > 13:
                continue
            sum = board[y][i] + board[y][i+1] + board[y][i+2] + board[y][i+3] + board[y][i+4] + board[y][i+5]
            if sum == 5 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[y][i+j] == 0:
                        tmp_lst.append((i+j, y))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)       
        # 위아래
        for i in range(y-5, y+1):
            if i < 0 or i > 13:
                continue
            sum = board[i][x] + board[i+1][x] + board[i+2][x] + board[i+3][x] + board[i+4][x] + board[i+5][x]
            if sum == 5 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[i+j][x] == 0:
                        tmp_lst.append((x, i+j))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
        # 왼쪽 위 오른쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y-5+i < 0 or x+i > 18 or y+i > 18:
                continue
            sum = board[y-5+i][x-5+i] + board[y-4+i][x-4+i] + board[y-3+i][x-3+i] + board[y-2+i][x-2+i] + board[y-1+i][x-1+i] + board[y+i][x+i]
            if sum == 5 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[y-j+i][x-j+i] == 0:
                        tmp_lst.append((x-j+i, y-j+i))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
        # 오른쪽 위 왼쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y+5-i > 18 or x+i > 18 or y-i < 0:
                continue
            sum = board[y+5-i][x-5+i] + board[y+4-i][x-4+i] + board[y+3-i][x-3+i] + board[y+2-i][x-2+i] + board[y+1-i][x-1+i] + board[y-i][x+i]
            if sum == 5 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[y+j-i][x-j+i] == 0:
                        tmp_lst.append((x-j+i, y+j-i))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
       
    if len(lst) != 0:
        lst = utils.get_max_open_point(1, board, lst)
        board[lst[0][1]][lst[0][0]] = 1
    
    return lst

def find_4stones_close(stone, board, left):
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
        # 양 옆
        for i in range(x-5, x+1):
            if i < 0 or i > 13:
                continue
            sum = board[y][i] + board[y][i+1] + board[y][i+2] + board[y][i+3] + board[y][i+4] + board[y][i+5]
            if sum == 4 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[y][i+j] == 0:
                        tmp_lst.append((i+j, y))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
        # 위아래
        for i in range(y-5, y+1):
            if i < 0 or i > 13:
                continue
            sum = board[i][x] + board[i+1][x] + board[i+2][x] + board[i+3][x] + board[i+4][x] + board[i+5][x]
            if sum == 4 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[i+j][x] == 0:
                        tmp_lst.append((x, i+j))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
        # 왼쪽 위 오른쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y-5+i < 0 or x+i > 18 or y+i > 18:
                continue
            sum = board[y-5+i][x-5+i] + board[y-4+i][x-4+i] + board[y-3+i][x-3+i] + board[y-2+i][x-2+i] + board[y-1+i][x-1+i] + board[y+i][x+i]
            if sum == 4 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[y-j+i][x-j+i] == 0:
                        tmp_lst.append((x-j+i, y-j+i))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
        # 오른쪽 위 왼쪽 아래 대각선
        for i in range(6):
            if x-5+i < 0 or y+5-i > 18 or x+i > 18 or y-i < 0:
                continue
            sum = board[y+5-i][x-5+i] + board[y+4-i][x-4+i] + board[y+3-i][x-3+i] + board[y+2-i][x-2+i] + board[y+1-i][x-1+i] + board[y-i][x+i]
            if sum == 4 * stone:
                tmp_lst = []
                for j in range(6):
                    if board[y+j-i][x-j+i] == 0:
                        tmp_lst.append((x-j+i, y+j-i))
                    if len(tmp_lst) != 0:
                        lst.extend(tmp_lst)
       
    if len(lst) != 0:
        lst = utils.get_max_open_points(1, board, lst)
    
    return lst