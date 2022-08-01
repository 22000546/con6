'''

'''
from CONNSIX import connsix
import ai 
import random 

def make_move(board):
	return chr(random.randint(65, 84)) + str(random.randint(1, 19)) + ":" + chr(random.randint(65, 84)) + str(random.randint(1, 19))

def num_to_coor(lst):
    result = ""

    for (x,y) in lst:
        if x > 8 :
            x += 1
        row = chr(x+65)
        col = y + 1 
        result.append(":"+row+str(col))
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