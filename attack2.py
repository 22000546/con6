import utils
import random


def attack_2(board, my_last_points, left):
    # 3-1 내가 돌 1개만 사용
	to_put = []
	if left == 2:
		# 일단 1개 써서 만들 수 있는 공격 있는지 해보고
		points = open3(board, my_last_points)
		# 있으면 거기 놓기로 하고
		if points != None:
			to_put.append(points)
			board[points[1]][points[0]] = 1
			left = left - 1
	# 남은 돌이 1개면 한번 더 찾아보기
	if left == 1:
		points = open3(board, my_last_points)
		# 남은 돌로 또 만들 수 있으면 그 점까지 넣고 총 2개 return, 없으면 그냥 1개만
		if points != None:
			to_put.append(points)
		return to_put
	#남은 돌이 2개면 1개로 못했던거니까 2개로 가능한지 알아보기
	elif left == 2:
		points = open2(board, my_last_points)
		# 2개로 공격할 수 있으면 그냥 그 points들 바로 return
		if points != None:
			return points
		# 2개로도 공격 못하면 그냥 빈거 return
		else:
			return to_put

	return to_put

def open3(board, my_last_points):
	candidate = set()
	for coor in my_last_points:
		(last_x, last_y) = coor
		# -방향
		if(last_x >= 2 and last_x <= 13):
			if(board[last_y][last_x-2]==0 and board[last_y][last_x-1]==0):
				if(board[last_y][last_x+1] + board[last_y][last_x+2] + board[last_y][last_x+3] == 2):
					if(board[last_y][last_x+4] == 0 and board[last_y][last_x+5] == 0):
						for i in range(last_x, last_x+4):
							if board[last_y][i] == 0:
								candidate.add((i, last_y))
		if(last_x >= 3 and last_x <= 14):
			if(board[last_y][last_x-3]==0 and board[last_y][last_x-2]==0):
				if(board[last_y][last_x-1] + board[last_y][last_x+1] + board[last_y][last_x+2] == 2):
					if(board[last_y][last_x+3] == 0 and board[last_y][last_x+4] == 0):
						for i in range(last_x-1, last_x+3):
							if board[last_y][i] == 0:
								candidate.add((i, last_y))
		if(last_x >= 4 and last_x <= 15):
			if(board[last_y][last_x-4]==0 and board[last_y][last_x-3]==0):
				if(board[last_y][last_x-2] + board[last_y][last_x-1] + board[last_y][last_x+1] == 2):
					if(board[last_y][last_x+2] == 0 and board[last_y][last_x+3] == 0):
						for i in range(last_x-2, last_x+2):
							if board[last_y][i] == 0:
								candidate.add((i, last_y))
		if(last_x >= 5 and last_x <= 16):
			if(board[last_y][last_x-5]==0 and board[last_y][last_x-4]==0):
				if(board[last_y][last_x-3] + board[last_y][last_x-2] + board[last_y][last_x-1] == 2):
					if(board[last_y][last_x+1] == 0 and board[last_y][last_x+2] == 0):
						for i in range(last_x-3, last_x+1):
							if board[last_y][i] == 0:
								candidate.add((i, last_y))
		# |방향
		if(last_y >= 2 and last_y <= 13):
			if(board[last_y-2][last_x]==0 and board[last_y-1][last_x]==0):
				if(board[last_y+1][last_x] + board[last_y+2][last_x] + board[last_y+3][last_x] == 2):
					if(board[last_y+4][last_x] == 0 and board[last_y+5][last_x] == 0):
						for i in range(last_y, last_y+4):
							if board[i][last_x] == 0:
								candidate.add((last_x, i))
		if(last_y >= 3 and last_y <= 14):
			if(board[last_y-3][last_x]==0 and board[last_y-2][last_x]==0):
				if(board[last_y-1][last_x] + board[last_y+1][last_x] + board[last_y+2][last_x] == 2):
					if(board[last_y+3][last_x] == 0 and board[last_y+4][last_x] == 0):
						for i in range(last_y-1, last_y+3):
							if board[i][last_x] == 0:
								candidate.add((last_x, i))
		if(last_y >= 4 and last_y <= 15):
			if(board[last_y-4][last_x]==0 and board[last_y-3][last_x]==0):
				if(board[last_y-2][last_x] + board[last_y-1][last_x] + board[last_y+1][last_x] == 2):
					if(board[last_y+2][last_x] == 0 and board[last_y+3][last_x] == 0):
						for i in range(last_y-2, last_y+2):
							if board[i][last_x] == 0:
								candidate.add((last_x, i))
		if(last_y >= 5 and last_y <= 16):
			if(board[last_y-5][last_x]==0 and board[last_y-4][last_x]==0):
				if(board[last_y-3][last_x] + board[last_y-2][last_x] + board[last_y-1][last_x] == 2):
					if(board[last_y+1][last_x] == 0 and board[last_y+2][last_x] == 0):
						for i in range(last_y-3, last_y+1):
							if board[i][last_x] == 0:
								candidate.add((last_x, i))
		# \방향
		if(last_x >= 2 and last_x <= 13 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x-2]==0 and board[last_y-1][last_x-1]==0):
				if(board[last_y+1][last_x+1] + board[last_y+2][last_x+2] + board[last_y+3][last_x+3] == 2):
					if(board[last_y+4][last_x+4] == 0 and board[last_y+5][last_x+5] == 0):
						for i in range(0, 4):
							if board[last_y+i][last_x+i] == 0:
								candidate.add((last_x+i, last_y+i))
		if(last_x >= 3 and last_x <= 14 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x-3]==0 and board[last_y-2][last_x-2]==0):
				if(board[last_y-1][last_x-1] + board[last_y+1][last_x+1] + board[last_y+2][last_x+2] == 2):
					if(board[last_y+3][last_x+3] == 0 and board[last_y+4][last_x+4] == 0):
						for i in range(-1, 3):
							if board[last_y+i][last_x+i] == 0:
								candidate.add((last_x+i, last_y+i))
		if(last_x >= 4 and last_x <= 15 and last_y >=4 and last_y <=15):
			if(board[last_y-4][last_x-4]==0 and board[last_y-3][last_x-3]==0):
				if(board[last_y-2][last_x-2] + board[last_y-1][last_x-1] + board[last_y+1][last_x+1] == 2):
					if(board[last_y+2][last_x+2] == 0 and board[last_y+3][last_x+3] == 0):
						for i in range(-2, 2):
							if board[last_y+i][last_x+i] == 0:
								candidate.add((last_x+i, last_y+i))
		if(last_x >= 5 and last_x <= 16 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x-5]==0 and board[last_y-4][last_x-4]==0):
				if(board[last_y-3][last_x-3] + board[last_y-2][last_x-2] + board[last_y-1][last_x-1] == 2):
					if(board[last_y+1][last_x+1] == 0 and board[last_y+2][last_x+2] == 0):
						for i in range(-3, 1):
							if board[last_y+i][last_x+i] == 0:
								candidate.add((last_x+i, last_y+i))
		# /방향
		if(last_x >= 5 and last_x <= 16 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x+2]==0 and board[last_y-1][last_x+1]==0):
				if(board[last_y+1][last_x-1] + board[last_y+2][last_x-2] + board[last_y+3][last_x-3] == 2):
					if(board[last_y+4][last_x-4] == 0 and board[last_y+5][last_x-5] == 0):
						for i in range(0, 4):
							if board[last_y+i][last_x-i] == 0:
								candidate.add((last_x-i, last_y+i))
		if(last_x >= 4 and last_x <= 15 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x+3]==0 and board[last_y-2][last_x+2]==0):
				if(board[last_y-1][last_x+1] + board[last_y+1][last_x-1] + board[last_y+2][last_x-2] == 2):
					if(board[last_y+3][last_x-3] == 0 and board[last_y+4][last_x-4] == 0):
						for i in range(-1, 3):
							if board[last_y+i][last_x-i] == 0:
								candidate.add((last_x-i, last_y+i))
		if(last_x >= 4 and last_x <= 14 and last_y >=4 and last_y <=14):
			if(board[last_y-4][last_x+4]==0 and board[last_y-3][last_x+3]==0):
				if(board[last_y-2][last_x+2] + board[last_y-1][last_x+1] + board[last_y+1][last_x-1] == 2):
					if(board[last_y+2][last_x-2] == 0 and board[last_y+3][last_x-3] == 0):
						for i in range(-2, 2):
							if board[last_y+i][last_x-i] == 0:
								candidate.add((last_x-i, last_y+i))
		if(last_x >= 2 and last_x <= 13 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x+5]==0 and board[last_y-4][last_x+4]==0):
				if(board[last_y-3][last_x+3] + board[last_y-2][last_x+2] + board[last_y-1][last_x+1] == 2):
					if(board[last_y+1][last_x-1] == 0 and board[last_y+2][last_x-2] == 0):
						for i in range(-3, 1):
							if board[last_y+i][last_x-i] == 0:
								candidate.add((last_x-i, last_y+i))
								#board[last_y+i][last_x-i] = 1
	if len(candidate):
		print("open3 candidate : " + str(candidate))
		return random.choice(list(candidate))
	else:
		return None

def open2(board, my_last_points):
	candidate = set()
	temp = []
	for coor in my_last_points:
		(last_x, last_y) = coor
			# -방향
		if(last_x >= 2 and last_x <= 13):
			if(board[last_y][last_x-2]==0 and board[last_y][last_x-1]==0):
				if(board[last_y][last_x+1] + board[last_y][last_x+2] + board[last_y][last_x+3] == 1):
					if(board[last_y][last_x+4] == 0 and board[last_y][last_x+5] == 0):
						for i in range(last_x, last_x+4):
							if board[last_y][i] == 0:
								temp.append((i, last_y))
								#board[last_y][i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 3 and last_x <= 14):
			if(board[last_y][last_x-3]==0 and board[last_y][last_x-2]==0):
				if(board[last_y][last_x-1] + board[last_y][last_x+1] + board[last_y][last_x+2] == 1):
					if(board[last_y][last_x+3] == 0 and board[last_y][last_x+4] == 0):
						for i in range(last_x-1, last_x+3):
							if board[last_y][i] == 0:
								temp.append((i, last_y))
								#board[last_y][i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 4 and last_x <= 15):
			if(board[last_y][last_x-4]==0 and board[last_y][last_x-3]==0):
				if(board[last_y][last_x-2] + board[last_y][last_x-1] + board[last_y][last_x+1] == 1):
					if(board[last_y][last_x+2] == 0 and board[last_y][last_x+3] == 0):
						for i in range(last_x-2, last_x+2):
							if board[last_y][i] == 0:
								temp.append((i, last_y))
								#board[last_y][i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 5 and last_x <= 16):
			if(board[last_y][last_x-5]==0 and board[last_y][last_x-4]==0):
				if(board[last_y][last_x-3] + board[last_y][last_x-2] + board[last_y][last_x-1] == 1):
					if(board[last_y][last_x+1] == 0 and board[last_y][last_x+2] == 0):
						for i in range(last_x-3, last_x+1):
							if board[last_y][i] == 0:
								temp.append((i, last_y))
								#board[last_y][i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		# |방향
		if(last_y >= 2 and last_y <= 13):
			if(board[last_y-2][last_x]==0 and board[last_y-1][last_x]==0):
				if(board[last_y+1][last_x] + board[last_y+2][last_x] + board[last_y+3][last_x] == 1):
					if(board[last_y+4][last_x] == 0 and board[last_y+5][last_x] == 0):
						for i in range(last_y, last_y+4):
							if board[i][last_x] == 0:
								temp.append((last_x, i))
								#board[i][last_x] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_y >= 3 and last_y <= 14):
			if(board[last_y-3][last_x]==0 and board[last_y-2][last_x]==0):
				if(board[last_y-1][last_x] + board[last_y+1][last_x] + board[last_y+2][last_x] == 1):
					if(board[last_y+3][last_x] == 0 and board[last_y+4][last_x] == 0):
						for i in range(last_y-1, last_y+3):
							if board[i][last_x] == 0:
								temp.append((last_x, i))
								#board[i][last_x] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_y >= 4 and last_y <= 15):
			if(board[last_y-4][last_x]==0 and board[last_y-3][last_x]==0):
				if(board[last_y-2][last_x] + board[last_y-1][last_x] + board[last_y+1][last_x] == 1):
					if(board[last_y+2][last_x] == 0 and board[last_y+3][last_x] == 0):
						for i in range(last_y-2, last_y+2):
							if board[i][last_x] == 0:
								temp.append((last_x, i))
								#board[i][last_x] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_y >= 5 and last_y <= 16):
			if(board[last_y-5][last_x]==0 and board[last_y-4][last_x]==0):
				if(board[last_y-3][last_x] + board[last_y-2][last_x] + board[last_y-1][last_x] == 1):
					if(board[last_y+1][last_x] == 0 and board[last_y+2][last_x] == 0):
						for i in range(last_y-3, last_y+1):
							if board[i][last_x] == 0:
								temp.append((last_x, i))
								#board[i][last_x] = 1
						candidate.add(tuple(temp))
						temp.clear()
		# \방향
		if(last_x >= 2 and last_x <= 13 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x-2]==0 and board[last_y-1][last_x-1]==0):
				if(board[last_y+1][last_x+1] + board[last_y+2][last_x+2] + board[last_y+3][last_x+3] == 1):
					if(board[last_y+4][last_x+4] == 0 and board[last_y+5][last_x+5] == 0):
						for i in range(0, 4):
							if board[last_y+i][last_x+i] == 0:
								temp.append((last_x+i, last_y+i))
								#board[last_y+i][last_x+i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 3 and last_x <= 14 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x-3]==0 and board[last_y-2][last_x-2]==0):
				if(board[last_y-1][last_x-1] + board[last_y+1][last_x+1] + board[last_y+2][last_x+2] == 1):
					if(board[last_y+3][last_x+3] == 0 and board[last_y+4][last_x+4] == 0):
						for i in range(-1, 3):
							if board[last_y+i][last_x+i] == 0:
								temp.append((last_x+i, last_y+i))
								#board[last_y+i][last_x+i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 4 and last_x <= 15 and last_y >=4 and last_y <=15):
			if(board[last_y-4][last_x-4]==0 and board[last_y-3][last_x-3]==0):
				if(board[last_y-2][last_x-2] + board[last_y-1][last_x-1] + board[last_y+1][last_x+1] == 1):
					if(board[last_y+2][last_x+2] == 0 and board[last_y+3][last_x+3] == 0):
						for i in range(-2, 2):
							if board[last_y+i][last_x+i] == 0:
								temp.append((last_x+i, last_y+i))
								#board[last_y+i][last_x+i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 5 and last_x <= 16 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x-5]==0 and board[last_y-4][last_x-4]==0):
				if(board[last_y-3][last_x-3] + board[last_y-2][last_x-2] + board[last_y-1][last_x-1] == 1):
					if(board[last_y+1][last_x+1] == 0 and board[last_y+2][last_x+2] == 0):
						for i in range(-3, 1):
							if board[last_y+i][last_x+i] == 0:
								temp.append((last_x+i, last_y+i))
								#board[last_y+i][last_x+i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		# /방향
		if(last_x >= 5 and last_x <= 16 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x+2]==0 and board[last_y-1][last_x+1]==0):
				if(board[last_y+1][last_x-1] + board[last_y+2][last_x-2] + board[last_y+3][last_x-3] == 1):
					if(board[last_y+4][last_x-4] == 0 and board[last_y+5][last_x-5] == 0):
						for i in range(0, 4):
							if board[last_y+i][last_x-i] == 0:
								temp.append((last_x-i, last_y+i))
								#board[last_y+i][last_x-i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 4 and last_x <= 15 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x+3]==0 and board[last_y-2][last_x+2]==0):
				if(board[last_y-1][last_x+1] + board[last_y+1][last_x-1] + board[last_y+2][last_x-2] == 1):
					if(board[last_y+3][last_x-3] == 0 and board[last_y+4][last_x-4] == 0):
						for i in range(-1, 3):
							if board[last_y+i][last_x-i] == 0:
								temp.append((last_x-i, last_y+i))
								#board[last_y+i][last_x-i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 4 and last_x <= 14 and last_y >=4 and last_y <=14):
			if(board[last_y-4][last_x+4]==0 and board[last_y-3][last_x+3]==0):
				if(board[last_y-2][last_x+2] + board[last_y-1][last_x+1] + board[last_y+1][last_x-1] == 1):
					if(board[last_y+2][last_x-2] == 0 and board[last_y+3][last_x-3] == 0):
						for i in range(-2, 2):
							if board[last_y+i][last_x-i] == 0:
								temp.append((last_x-i, last_y+i))
								#board[last_y+i][last_x-i] = 1
						candidate.add(tuple(temp))
						temp.clear()
		if(last_x >= 2 and last_x <= 13 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x+5]==0 and board[last_y-4][last_x+4]==0):
				if(board[last_y-3][last_x+3] + board[last_y-2][last_x+2] + board[last_y-1][last_x+1] == 1):
					if(board[last_y+1][last_x-1] == 0 and board[last_y+2][last_x-2] == 0):
						for i in range(-3, 1):
							if board[last_y+i][last_x-i] == 0:
								temp.append((last_x-i, last_y+i))
								#board[last_y+i][last_x-i] = 1
						candidate.add(tuple(temp))
						temp.clear()
	if len(candidate):
		print("open2 candidate : " + str(candidate))
		return random.choice(list(candidate))
	else:
		return None
