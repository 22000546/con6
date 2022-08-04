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
    attack_points = attack_points2 | attack_points3
    defense_points2 = attack2.open2(10, board, away_move_log) # 상대방의 열린 2개를 막을 수 있는 지점
    # print("defense2", defense_points2)
    defense_points3 = attack2.open3(10, board, away_move_log) # 상대방의 열린 3개를 막을 수 있는 지점 
    # print("defense3", defense_points3)
    defense_points = defense_points2 | defense_points3 # 두 지점의 합집합 
    # print("defense", defense_points)
    intersect_points = attack_points & defense_points # 두 지점의 교집합
    # print("intersect", intersect_points)
    
    if len(intersect_points) == 0:
        if len(defense_points) == 0:
            lst = list(attack_points)
            if len(lst) == 0:
                return lst
            else:
                print("attack")
        else:
            lst = list(defense_points)
            print("defense")
        lst = utils.get_max_open_point(1, board, lst)
        board[lst[0][1]][lst[0][0]] = 1
        return lst
    
    lst = utils.get_max_open_point(1, board, list(intersect_points))
    board[lst[0][1]][lst[0][0]] = 1
    print("attack + defense")
    
    return lst