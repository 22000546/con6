import random
from itertools import combinations

def diagonal_RD_search(x, y, num, find): # left top to right down 
    flag = sum = 0
    RD = []
    for i in range(num-1, -1, -1):
        # case : y-i, x-i 
        print(y-i, x-i )
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

        if sum == find:
            RD.append((x-i,y-i))

    print("RD", RD)
    
    res = []
    if len(RD) > 0:
        if find == 3:
            [res.append((x+j, y+j)) for (x,y) in RD for j in range(0, num) if board[y+j][x+j] == 0]
        elif find == 2:
            items = []
            [items.append((x+j, y+j)) for (x,y) in RD for j in range(0, num) if board[y+j][x+j] == 0]
            res.extend(list(combinations(items, 2)))

    return res

def diagonal_RU_search(x, y, num, find): # left bottom to right up 
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
    
    print("RU", RU)
    
    res = []
    if len(RU) > 0:
        if find == 3: 
            [res.append((x+j, y-j)) for (x,y) in RU for j in range(0, num) if board[y-j][x+j]==0]
        elif find == 2:
            items = []
            [items.append((x+j, y-j)) for (x,y) in RU for j in range(0, num) if board[y-j][x+j] == 0]
            res.extend(list(combinations(items, 2)))
    return res

def horizontal_search(x, y, num, find):  # left to right 
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
        
    print("hori", hori)
    
    res = []
    if len(hori) > 0:
        if find == 3:
            [res.append((x+j, y)) for (x,y) in hori for j in range(0, num) if board[y][x+j] == 0]
        elif find == 2:
            items = []
            [items.append((x+j, y)) for (x,y) in hori for j in range(0, num) if board[y][x+j] == 0]
            res.extend(list(combinations(items, 2)))
    return res

def vertical_search(x, y, num, find): # top to bottom 
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
    
    print("ver", ver)
    
    res = []
    if len(ver) > 0:
        if find == 3:
            [res.append((x,y+j)) for (x,y) in ver for j in range(0, num) if board[y+j][x] == 0]
        elif find == 2:
            items = []
            [items.append((x, y+j)) for (x,y) in ver for j in range(0, num) if board[y+j][x] == 0]
            res.extend(list(combinations(items, 2)))
    return res


def algo4(left, stone, board):
    # find 3stones close 
    ret = []
    while left > 0 :
        res = find_3stones_close(stone, board)
        rand = random.randint(0,len(res)-1)
        x,y = res[rand]
        board[y][x] = 1
        ret.append((x,y))
        left -= 1
    return ret 


def find_2stones_close(stone, board):
    global last_ai_move, last_away_move

    lst = []

    if stone == 1: # find ai stones 
        if last_ai_move == None:
            print("first time to place ai stones")
            return None
        else :
            for (x,y) in last_ai_move:
                # print((x,y),"-----------------------------------")
                hori = horizontal_search(x, y, 6, 2)
                lst.extend(hori)
                # print("hori res", hori)

                ver = vertical_search(x, y, 6, 2)
                lst.extend(ver)
                # print("ver res", ver)

                RU = diagonal_RU_search(x, y, 6, 2)
                lst.extend(RU)
                # print("RU res", RU)

                RD = diagonal_RD_search(x, y, 6, 2)
                lst.extend(RD)
                # print("RD res", RD)
    # else : # find away stones 

    return lst

def find_3stones_close(stone, board):
    global last_ai_move, last_away_move

    lst = []

    if stone == 1: # find ai stones 
        if last_ai_move == None:
            print("first time to place ai stones")
            return None
        else :
            for (x,y) in last_ai_move:
                # print((x,y),"-----------------------------------")
                hori = horizontal_search(x, y, 6, 3)
                lst.extend(hori)
                # print("hori res", hori)

                ver = vertical_search(x,y, 6, 3)
                lst.extend(ver)
                # print("ver res", ver)

                RU = diagonal_RU_search(x,y, 6, 3)
                lst.extend(RU)
                # print("RU res", RU)

                RD = diagonal_RD_search(x,y, 6, 3)
                lst.extend(RD)
                # print("RD res", RD)

    # else : # find away stones 

    return lst