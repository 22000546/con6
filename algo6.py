import random
import utils
import attack2

def algo6(stone, board, left):
    result = find_defense_and_attack(board, left)
    left -= len(result)
    
    if left > 0:
        result += find_defense_and_attack(board, left)
        left -= len(result)
    
    return result

def find_defense_and_attack(board, left):
    ai_move_log = utils.get_ai_move_log()
    away_move_log = utils.get_away_move_log()
    lst = []
    
    if left == 0:
        return lst
    
    attack_points = attack2.open2(0, board, ai_move_log) # 열린 1 -> 2로 만들 수 있는 지점
    defense_points = attack2.open2(10, board, away_move_log) # 상대방의 열린 2개를 막을 수 있는 지점
    intersect_points = attack_points & defense_points # 두 지점의 교집합
    
    if len(intersect_points) == 0:
        if len(attack_points) == 0:
            lst = defense_points
        else:
            select = random.randint(0, len(attack_points)-1)
            lst = list(attack_points)
            lst = lst[select]
            board[lst[0][1]][lst[0][0]] = 1
    
    max_open = -1
    for point in intersect_points:
        board[point[1]][point[0]] = 1
        tmp = attack2.open2(1, board, ai_move_log)
        if len(tmp) > max_open:
            max_open = len(tmp)
            max_point = point
        board[point[1]][point[0]] = 0
    
    lst = list(max_point)
    board[lst[0][1]][lst[0][0]] = 1
        
    return lst