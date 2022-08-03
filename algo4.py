import random
from itertools import combinations
import utils 

def check_5stones(board, x, y):
    # 내가 돌을 놨을 때 8방향으로 내 돌 5개+빈칸 인 경우가 만들어 지는지 확인 
    ret = 0
    ret += left_right_5(board, x, y, "RD")
    ret += left_right_5(board, x, y, "RU")
    ret += left_right_5(board, x, y, "hori")
    ret += left_right_5(board, x, y, "ver")
    return ret 

def left_right_5(board, x, y, direction):

    for i in range(6, -1, -1):
        sum = 1 
        for j in range(0,8):
            try:
                if sum >= 10 : # 중간에 user stone or red stone 만나면 그만 
                    break 
                if direction == "RD":
                    sum += board[y-i+j][x-i+j]
                elif direction == "RU":
                    sum += board[y+i-j][x-i+j]
                elif direction == "hori":
                    sum += board[y][x-i+j]
                elif direction == "ver":
                    sum += board[y-i+j][x]
            except IndexError:
                break 
        if sum % 10 >= 5 :
            return 1
    return 0 
                
def diagonal_RD_search(board, x, y, num, find): # left top to right down 
    flag = sum = 0
    RD = []
    for i in range(num-1, -1, -1):
        # case : y-i, x-i 
        if y-i+(num-1) > 18 or x-i+(num-1) > 18:
            break
        if y-i > 18 or y-i < 0 or x-i > 18 or x-i < 0:
            continue 
        if flag == 0:
            flag = 1
            for j in range(0, num):
                sum += board[y-i+j][x-i+j] 
        else:
            sum = sum - board[y-i-1][x-i-1] + board[y-i+(num-1)][x-i+(num-1)]
        
        if sum == find :
            RD.append((x-i,y-i))

    if len(RD) > 0:
        print("RD", RD, "x,y", x, y)
    
    res = []
    if len(RD) > 0:
        if find == 3:
            [res.append((x+j, y+j)) for (x,y) in RD for j in range(0, num) if board[y+j][x+j] == 0 and check_5stones(board, x+j, y+j) == 0]
        elif find == 2:
            items = set()
            [items.add((x+j, y+j)) for (x,y) in RD for j in range(0, num) if board[y+j][x+j] == 0]
            res.append(list(combinations(list(items), 2)))

    return res

def diagonal_RU_search(board, x, y, num, find): # left bottom to right up 
    flag = sum = 0
    RU = []
    for i in range(num-1, -1, -1):
        # case : y+i, x-i 
        if y+i-(num-1) > 18 or x-i+(num-1) > 18:
            break
        if y+i > 18 or y+i < 0 or x-i > 18 or x-i < 0:
            continue 
        if flag == 0:
            flag = 1
            for j in range(0, num):
                sum += board[y+i-j][x-i+j]
        else:
            sum = sum - board[y+i+1][x-i-1] + board[y+i-(num-1)][x-i+(num-1)]
        if sum == find:
            RU.append((x-i,y+i))
    
    if len(RU) > 0:
        print("RU", RU, "x,y", x, y)
    
    res = []
    if len(RU) > 0:
        if find == 3: 
            [res.append((x+j, y-j)) for (x,y) in RU for j in range(0, num) if board[y-j][x+j] == 0 and check_5stones(board, x+j, y-j) == 0]
        elif find == 2:
            items = set()
            [items.add((x+j, y-j)) for (x,y) in RU for j in range(0, num) if board[y-j][x+j] == 0]
            res.append(list(combinations(list(items), 2)))
    return res

def horizontal_search(board, x, y, num, find):  # left to right 
    flag = sum = 0
    hori = []
    for i in range(num-1, -1, -1):
        if x-i+(num-1) > 18 :
            break
        if x-i > 18 or x-i < 0 :
            continue 
        if flag == 0:
            flag = 1
            for j in range(0, num):
                sum += board[y][x-i+j]
        else:
            sum = sum - board[y][x-i-1] + board[y][x-i+(num-1)]
        if sum == find:
            hori.append((x-i,y))
        
    if len(hori) > 0 :
        print("hori", hori, "x,y", x, y)
    
    res = []
    if len(hori) > 0:
        if find == 3:
            [res.append((x+j, y)) for (x,y) in hori for j in range(0, num) if board[y][x+j] == 0 and  check_5stones(board, x+j, y) == 0]
        elif find == 2:
            items = set()
            [items.add((x+j, y)) for (x,y) in hori for j in range(0, num) if board[y][x+j] == 0]
            res.append(list(combinations(list(items), 2)))
    return res

def vertical_search(board, x, y, num, find): # top to bottom 
    flag = sum = 0
    ver = [] # starting point of pattern 
    for i in range(num-1, -1, -1):
        if y-i+(num-1) > 18 :
            break
        if y-i > 18 or y-i < 0 :
            continue 
        if flag == 0:
            flag = 1
            for j in range(0, num):
                sum += board[y-i+j][x]
        else:
            sum = sum - board[y-i-1][x] + board[y-i+(num-1)][x]
        if sum == find:
            ver.append((x,y-i))
    
    if len(ver) >0 :
        print("ver", ver, "x,y", x, y)
    
    res = []
    if len(ver) > 0:
        if find == 3:
            [res.append((x,y+j)) for (x,y) in ver for j in range(0, num) if board[y+j][x] == 0 and  check_5stones(board, x, y+j) == 0]
        elif find == 2:
            items = set()
            [items.add((x, y+j)) for (x,y) in ver for j in range(0, num) if board[y+j][x] == 0]
            res.append(list(combinations(list(items), 2)))
    return res


def algo4(left, stone, board):
    
    ret = []

    # find 3stones close 
    while left > 0 :
        res = find_3stones_close(stone, board)
        if len(res) == 0:
            break
        rand = random.randint(0, len(res)-1)
        x,y = res[rand]
        board[y][x] = 1
        ret.append((x,y))
        left -= 1
    
    # find 2stones close 
    if left == 2:
        res = find_2stones_close(stone, board)
        if len(res) == 0:
            return ret 
        print("find 2stones close")
        select_set = random.randint(0, len(res)-1)
        rand = random.randint(0, len(res[select_set])-1)
        (x,y),(x1,y1) = res[select_set][rand]
        board[y][x] = 1
        board[y1][x1] = 1
        ret.append((x,y))
        ret.append((x1,y1))
    return ret 

def find_3stones_close(stone, board):
    last_ai_move = utils.get_ai_move()
    last_away_move = utils.get_away_move()

    lst = []

    if stone == 1: # find ai stones 
        if last_ai_move == None:
            print("first time to place ai stones")
            return lst
        else :
            for (x,y) in last_ai_move:
                # print((x,y),"-----------------------------------")
                hori = horizontal_search(board, x, y, 6, 3)
                lst.extend(hori)
                # print("hori res", hori)

                ver = vertical_search(board, x,y, 6, 3)
                lst.extend(ver)
                # print("ver res", ver)

                RU = diagonal_RU_search(board, x,y, 6, 3)
                lst.extend(RU)
                # print("RU res", RU)

                RD = diagonal_RD_search(board, x,y, 6, 3)
                lst.extend(RD)
                # print("RD res", RD)

    # else : # find away stones 

    return lst

def find_2stones_close(stone, board):
    last_ai_move = utils.get_ai_move()
    last_away_move = utils.get_away_move()

    lst = []

    if stone == 1: # find ai stones 
        if last_ai_move == None:
            print("first time to place ai stones")
            return lst 
        else :
            for (x,y) in last_ai_move:
                # print((x,y),"-----------------------------------")
                hori = horizontal_search(board, x, y, 6, 2)
                lst.extend(hori)
                # print("hori res", hori)

                ver = vertical_search(board, x, y, 6, 2)
                lst.extend(ver)
                # print("ver res", ver)

                RU = diagonal_RU_search(board, x, y, 6, 2)
                lst.extend(RU)
                # print("RU res", RU)

                RD = diagonal_RD_search(board, x, y, 6, 2)
                lst.extend(RD)
                # print("RD res", RD)
    # else : # find away stones 

    return lst