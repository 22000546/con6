import utils
import attack2

def algo6(board, left):
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
    
    attack_points2 = attack2.open2(0, board, ai_move_log) # 열린 1 -> 2로 만들 수 있는 지점
    # print("attack2", attack_points2)
    attack_points3_two = attack2.open2(1, board, ai_move_log) # 열린 2 -> 3으로 만들 수 있는 지점
    attack_points3 = set()
    for (p1, p2) in attack_points3_two:
        attack_points3.add(p1)
        attack_points3.add(p2)
    # print("attack3", attack_points3)
    defense_points2 = attack2.open2(10, board, away_move_log) # 상대방의 열린 2개를 막을 수 있는 지점
    # print("defense2", defense_points2)
    defense_points3 = attack2.open3(10, board, away_move_log) # 상대방의 열린 3개를 막을 수 있는 지점 
    # print("defense3", defense_points3)
    
    
    intersect1 = attack_points3 & defense_points3
    intersect2 = attack_points2 & defense_points3
    intersect3 = attack_points3 & defense_points2
    intersect4 = attack_points2 & defense_points2
    
    # attack3 + defense3
    if len(intersect1) > 0:
        lst = utils.get_max_open_point(1, board, list(intersect1))
        board[lst[0][1]][lst[0][0]] = 1
        print("attack3 + defense3")
    elif len(intersect2) > 0:
        lst = utils.get_max_open_point(1, board, list(intersect2))
        board[lst[0][1]][lst[0][0]] = 1
        print("attack2 + defense3")
    elif len(intersect3) > 0:
        lst = utils.get_max_open_point(1, board, list(intersect3))
        board[lst[0][1]][lst[0][0]] = 1
        print("attack3 + defense2")
    elif len(intersect4) > 0:
        lst = utils.get_max_open_point(1, board, list(intersect4))
        board[lst[0][1]][lst[0][0]] = 1
        print("attack2 + defense2")
    elif len(defense_points3) > 0:
        lst = utils.get_max_open_point(1, board, list(defense_points3))
        board[lst[0][1]][lst[0][0]] = 1
        print("defense3")
    elif len(defense_points2) > 0:
        lst = utils.get_max_open_point(1, board, list(defense_points2))
        board[lst[0][1]][lst[0][0]] = 1
        print("defense2")
    elif len(attack_points3) + len(attack_points2) > 0:
        attack_points = attack_points2 | attack_points3
        lst = utils.get_max_open_point(1, board, list(attack_points))
        board[lst[0][1]][lst[0][0]] = 1
        print("attack2 or 3")
    
    return lst