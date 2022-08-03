from itertools import combinations
import attack2

def find_open(board, point):
    open = 0
    total_open = 0
    for i in range(6):
        if board[point[1]-i][point[0]] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]+i][point[0]] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]-i][point[0]-i] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]-i][point[0]+i] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]+i][point[0]-i] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]+i][point[0]+i] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]][point[0]-i] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    for i in range(6):
        if board[point[1]][point[0]+i] != 100:
            open += 1
        else:
            open = 0
    total_open += open
    open = 0
    
    return total_open

def find_first(board):
    cand = [(8,8), (8,9), (8,10), (9,8), (9,10), (10,8), (10,9), (10,10)]
    lst = list(combinations(cand, 2))
    max_len = 0
    max_open = 0
    final_result = None
    
    for (x1, y1), (x2, y2) in lst:
        if board[y1][x1] != 0 or board[y2][x2] != 0:
            continue
        board[y1][x1] = 1
        board[y2][x2] = 1
        result = attack2.open2(1, board, [(x1, y1), (x2, y2)])
        open_score = find_open(board, (x1, y1)) + find_open(board, (x2, y2))
        if len(result) >= max_len and open_score > max_open:
            max_len = len(result)
            max_open = open_score
            final_result = [(x1, y1), (x2, y2)]
        board[y1][x1] = 0
        board[y2][x2] = 0
            
    return final_result
