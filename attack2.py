import utils

def attack_2(board, my_last_points, left):
    # 3-1 내가 돌 1개만 사용
	to_put = []
	if left ==0:
		return to_put
	if left == 2:
		# 일단 1개 써서 만들 수 있는 공격 있는지 해보고
		points = open3(1, board, my_last_points)
		# 있으면 거기 놓기로 하고
		if len(points) > 0:
			points = utils.get_max_open_point(1, board, list(points))
			to_put.extend(points)
			board[points[0][1]][points[0][0]] = 1
			left = left - 1
	# 남은 돌이 1개면 한번 더 찾아보기
	if left == 1:
		points = open3(1, board, my_last_points)
		# 남은 돌로 또 만들 수 있으면 그 점까지 넣고 총 2개 return, 없으면 그냥 1개만
		if len(points) > 0:
			points = utils.get_max_open_point(1, board, list(points))
			to_put.extend(points)
		return to_put
	#남은 돌이 2개면 1개로 못했던거니까 2개로 가능한지 알아보기
	elif left == 2:
		points = open2(1, board, my_last_points)
		# 2개로 공격할 수 있으면 그냥 그 points들 바로 return
		if len(points) > 0:
        	#print("open2 candidate : " + str(candidate))
			points = utils.get_max_open_points(1, board, list(points))
			return points
		# 2개로도 공격 못하면 그냥 빈거 return
		else:
			return to_put

	return to_put

def open3(stone, board, my_last_points):
	candidate = set()
	temp = []
	for coor in my_last_points:
		(last_x, last_y) = coor
		# -방향
		if(last_x >= 2 and last_x <= 13):
			if(board[last_y][last_x-2]==0 and board[last_y][last_x-1]==0):
				if(board[last_y][last_x+1] + board[last_y][last_x+2] + board[last_y][last_x+3] == 2*stone):
					if(board[last_y][last_x+4] == 0 and board[last_y][last_x+5] == 0):
						if stone == 1:
							for i in range(last_x, last_x+4):
								if board[last_y][i] == 0:
									candidate.add((i, last_y))
						elif stone == 10:
							# 상대방 돌 주위 2칸 이내 
							for i in range(last_x, last_x+4):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
		if(last_x >= 3 and last_x <= 14):
			if(board[last_y][last_x-3]==0 and board[last_y][last_x-2]==0):
				if(board[last_y][last_x-1] + board[last_y][last_x+1] + board[last_y][last_x+2] == 2*stone):
					if(board[last_y][last_x+3] == 0 and board[last_y][last_x+4] == 0):
						if stone == 1:
							for i in range(last_x-1, last_x+3):
								if board[last_y][i] == 0:
									candidate.add((i, last_y))
						elif stone == 10:
							for i in range(last_x-1, last_x+3):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
		if(last_x >= 4 and last_x <= 15):
			if(board[last_y][last_x-4]==0 and board[last_y][last_x-3]==0):
				if(board[last_y][last_x-2] + board[last_y][last_x-1] + board[last_y][last_x+1] == 2*stone):
					if(board[last_y][last_x+2] == 0 and board[last_y][last_x+3] == 0):
						if stone == 1:
							for i in range(last_x-2, last_x+2):
								if board[last_y][i] == 0:
									candidate.add((i, last_y))
						elif stone == 10:
							for i in range(last_x-2, last_x+2):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
		if(last_x >= 5 and last_x <= 16):
			if(board[last_y][last_x-5]==0 and board[last_y][last_x-4]==0):
				if(board[last_y][last_x-3] + board[last_y][last_x-2] + board[last_y][last_x-1] == 2*stone):
					if(board[last_y][last_x+1] == 0 and board[last_y][last_x+2] == 0):
						if stone == 1:
							for i in range(last_x-3, last_x+1):
								if board[last_y][i] == 0:
									candidate.add((i, last_y))
						elif stone == 10:
							for i in range(last_x-3, last_x+1):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
		# |방향
		if(last_y >= 2 and last_y <= 13):
			if(board[last_y-2][last_x]==0 and board[last_y-1][last_x]==0):
				if(board[last_y+1][last_x] + board[last_y+2][last_x] + board[last_y+3][last_x] == 2*stone):
					if(board[last_y+4][last_x] == 0 and board[last_y+5][last_x] == 0):
						if stone == 1:
							for i in range(last_y, last_y+4):
								if board[i][last_x] == 0:
									candidate.add((last_x, i))
						elif stone == 10:
							for i in range(last_y, last_y+4):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
		if(last_y >= 3 and last_y <= 14):
			if(board[last_y-3][last_x]==0 and board[last_y-2][last_x]==0):
				if(board[last_y-1][last_x] + board[last_y+1][last_x] + board[last_y+2][last_x] == 2*stone):
					if(board[last_y+3][last_x] == 0 and board[last_y+4][last_x] == 0):
						if stone == 1:
							for i in range(last_y-1, last_y+3):
								if board[i][last_x] == 0:
									candidate.add((last_x, i))
						elif stone == 10:
							for i in range(last_y-1, last_y+3):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
		if(last_y >= 4 and last_y <= 15):
			if(board[last_y-4][last_x]==0 and board[last_y-3][last_x]==0):
				if(board[last_y-2][last_x] + board[last_y-1][last_x] + board[last_y+1][last_x] == 2*stone):
					if(board[last_y+2][last_x] == 0 and board[last_y+3][last_x] == 0):
						if stone == 1:
							for i in range(last_y-2, last_y+2):
								if board[i][last_x] == 0:
									candidate.add((last_x, i))
						elif stone == 10:
							for i in range(last_y-2, last_y+2):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
		if(last_y >= 5 and last_y <= 16):
			if(board[last_y-5][last_x]==0 and board[last_y-4][last_x]==0):
				if(board[last_y-3][last_x] + board[last_y-2][last_x] + board[last_y-1][last_x] == 2*stone):
					if(board[last_y+1][last_x] == 0 and board[last_y+2][last_x] == 0):
						if stone == 1:
							for i in range(last_y-3, last_y+1):
								if board[i][last_x] == 0:
									candidate.add((last_x, i))
						elif stone == 10:
							for i in range(last_y-3, last_y+1):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
		# \방향
		if(last_x >= 2 and last_x <= 13 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x-2]==0 and board[last_y-1][last_x-1]==0):
				if(board[last_y+1][last_x+1] + board[last_y+2][last_x+2] + board[last_y+3][last_x+3] == 2*stone):
					if(board[last_y+4][last_x+4] == 0 and board[last_y+5][last_x+5] == 0):
						if stone == 1:
							for i in range(0, 4):
								if board[last_y+i][last_x+i] == 0:
									candidate.add((last_x+i, last_y+i))
						elif stone == 10:
							for i in range(0,4):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
		if(last_x >= 3 and last_x <= 14 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x-3]==0 and board[last_y-2][last_x-2]==0):
				if(board[last_y-1][last_x-1] + board[last_y+1][last_x+1] + board[last_y+2][last_x+2] == 2*stone):
					if(board[last_y+3][last_x+3] == 0 and board[last_y+4][last_x+4] == 0):
						if stone == 1:
							for i in range(-1, 3):
								if board[last_y+i][last_x+i] == 0:
									candidate.add((last_x+i, last_y+i))
						elif stone == 10:
							for i in range(-1, 3):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
		if(last_x >= 4 and last_x <= 15 and last_y >=4 and last_y <=15):
			if(board[last_y-4][last_x-4]==0 and board[last_y-3][last_x-3]==0):
				if(board[last_y-2][last_x-2] + board[last_y-1][last_x-1] + board[last_y+1][last_x+1] == 2*stone):
					if(board[last_y+2][last_x+2] == 0 and board[last_y+3][last_x+3] == 0):
						if stone == 1:
							for i in range(-2, 2):
								if board[last_y+i][last_x+i] == 0:
									candidate.add((last_x+i, last_y+i))
					elif stone == 10:
							for i in range(-2, 2):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
		if(last_x >= 5 and last_x <= 16 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x-5]==0 and board[last_y-4][last_x-4]==0):
				if(board[last_y-3][last_x-3] + board[last_y-2][last_x-2] + board[last_y-1][last_x-1] == 2*stone):
					if(board[last_y+1][last_x+1] == 0 and board[last_y+2][last_x+2] == 0):
						if stone == 1:
							for i in range(-3, 1):
								if board[last_y+i][last_x+i] == 0:
									candidate.add((last_x+i, last_y+i))
						elif stone == 10:
							for i in range(-3, 1):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
		# /방향
		if(last_x >= 5 and last_x <= 16 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x+2]==0 and board[last_y-1][last_x+1]==0):
				if(board[last_y+1][last_x-1] + board[last_y+2][last_x-2] + board[last_y+3][last_x-3] == 2*stone):
					if(board[last_y+4][last_x-4] == 0 and board[last_y+5][last_x-5] == 0):
						if stone == 1:
							for i in range(0, 4):
								if board[last_y+i][last_x-i] == 0:
									candidate.add((last_x-i, last_y+i))
						elif stone == 10:
							for i in range(0,4):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
		if(last_x >= 4 and last_x <= 15 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x+3]==0 and board[last_y-2][last_x+2]==0):
				if(board[last_y-1][last_x+1] + board[last_y+1][last_x-1] + board[last_y+2][last_x-2] == 2*stone):
					if(board[last_y+3][last_x-3] == 0 and board[last_y+4][last_x-4] == 0):
						if stone == 1:
							for i in range(-1, 3):
								if board[last_y+i][last_x-i] == 0:
									candidate.add((last_x-i, last_y+i))
						elif stone == 10:
							for i in range(-1, 3):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
		if(last_x >= 4 and last_x <= 14 and last_y >=4 and last_y <=14):
			if(board[last_y-4][last_x+4]==0 and board[last_y-3][last_x+3]==0):
				if(board[last_y-2][last_x+2] + board[last_y-1][last_x+1] + board[last_y+1][last_x-1] == 2*stone):
					if(board[last_y+2][last_x-2] == 0 and board[last_y+3][last_x-3] == 0):
						if stone == 1:
							for i in range(-2, 2):
								if board[last_y+i][last_x-i] == 0:
									candidate.add((last_x-i, last_y+i))
						elif stone == 10:
							for i in range(-2, 2):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
		if(last_x >= 2 and last_x <= 13 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x+5]==0 and board[last_y-4][last_x+4]==0):
				if(board[last_y-3][last_x+3] + board[last_y-2][last_x+2] + board[last_y-1][last_x+1] == 2*stone):
					if(board[last_y+1][last_x-1] == 0 and board[last_y+2][last_x-2] == 0):
						if stone == 1:
							for i in range(-3, 1):
								if board[last_y+i][last_x-i] == 0:
									candidate.add((last_x-i, last_y+i))
									#board[last_y+i][last_x-i] = 1
						elif stone == 10:
							for i in range(-3, 1):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
	return candidate

def open2(stone, board, my_last_points):
	# stone 10일 때는 3번째 인자 away_move로 주어야 함 ! 
	candidate = set()
	temp = [] 
	for coor in my_last_points:
		(last_x, last_y) = coor
			# -방향
		if(last_x >= 2 and last_x <= 13): # 가운데 4칸 중에 내가 놓은 돌 or 상대방 돌이 첫번째인 경우 
			if(board[last_y][last_x-2]==0 and board[last_y][last_x-1]==0):
				if(board[last_y][last_x+1] + board[last_y][last_x+2] + board[last_y][last_x+3] == 1*stone):
					if(board[last_y][last_x+4] == 0 and board[last_y][last_x+5] == 0):
						if stone == 1:
							for i in range(last_x, last_x+4):
								if board[last_y][i] == 0:
									temp.append((i, last_y))
									#board[last_y][i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10 :
							# 상대방 돌 주위 2칸 이내 
							for i in range(last_x, last_x+4):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
						elif stone == 0 : 
							candidate.update([(last_x+1,last_y),(last_x+2,last_y),(last_x+3,last_y)])
		if(last_x >= 3 and last_x <= 14): # 가운데 4칸 중에 내가 놓은 돌이 두 번째 
			if(board[last_y][last_x-3]==0 and board[last_y][last_x-2]==0):
				if(board[last_y][last_x-1] + board[last_y][last_x+1] + board[last_y][last_x+2] == 1*stone):
					if(board[last_y][last_x+3] == 0 and board[last_y][last_x+4] == 0):
						if stone == 1: 
							for i in range(last_x-1, last_x+3):
								if board[last_y][i] == 0:
									temp.append((i, last_y))
									#board[last_y][i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_x-1, last_x+3):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
						elif stone == 0 : 
							candidate.update([(last_x-1,last_y),(last_x+1,last_y),(last_x+2,last_y)])
		if(last_x >= 4 and last_x <= 15): # 가운데 4칸 중에 내가 놓은 돌이 세 번째 
			if(board[last_y][last_x-4]==0 and board[last_y][last_x-3]==0):
				if(board[last_y][last_x-2] + board[last_y][last_x-1] + board[last_y][last_x+1] == 1*stone):
					if(board[last_y][last_x+2] == 0 and board[last_y][last_x+3] == 0):
						if stone == 1:
							for i in range(last_x-2, last_x+2):
								if board[last_y][i] == 0:
									temp.append((i, last_y))
									#board[last_y][i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_x-2, last_x+2):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
						elif stone == 0 : 
							candidate.update([(last_x-2,last_y),(last_x-1,last_y),(last_x+1,last_y)])
		if(last_x >= 5 and last_x <= 16): # 가운데 4칸 중에 내가 놓은 돌이 네 번째 
			if(board[last_y][last_x-5]==0 and board[last_y][last_x-4]==0):
				if(board[last_y][last_x-3] + board[last_y][last_x-2] + board[last_y][last_x-1] == 1*stone):
					if(board[last_y][last_x+1] == 0 and board[last_y][last_x+2] == 0):
						if stone == 1:
							for i in range(last_x-3, last_x+1):
								if board[last_y][i] == 0:
									temp.append((i, last_y))
									#board[last_y][i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_x-3, last_x+1):
								if board[last_y][i] == stone:
									temp.append((i, last_y))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y][x+j] == 0:
										candidate.add((x+j, y))
							temp.clear()
						elif stone == 0 : 
							candidate.update([(last_x-3,last_y),(last_x-2,last_y),(last_x-1,last_y)])
		# |방향
		if(last_y >= 2 and last_y <= 13):
			if(board[last_y-2][last_x]==0 and board[last_y-1][last_x]==0):
				if(board[last_y+1][last_x] + board[last_y+2][last_x] + board[last_y+3][last_x] == 1*stone):
					if(board[last_y+4][last_x] == 0 and board[last_y+5][last_x] == 0):
						if stone == 1 :
							for i in range(last_y, last_y+4):
								if board[i][last_x] == 0:
									temp.append((last_x, i))
									#board[i][last_x] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_y, last_y+4):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x, last_y+1), (last_x, last_y+2), (last_x, last_y+3)])
		if(last_y >= 3 and last_y <= 14):
			if(board[last_y-3][last_x]==0 and board[last_y-2][last_x]==0):
				if(board[last_y-1][last_x] + board[last_y+1][last_x] + board[last_y+2][last_x] == 1*stone):
					if(board[last_y+3][last_x] == 0 and board[last_y+4][last_x] == 0):
						if stone == 1:
							for i in range(last_y-1, last_y+3):
								if board[i][last_x] == 0:
									temp.append((last_x, i))
									#board[i][last_x] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_y-1, last_y+3):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x, last_y-1), (last_x, last_y+1), (last_x, last_y+2)])
		if(last_y >= 4 and last_y <= 15):
			if(board[last_y-4][last_x]==0 and board[last_y-3][last_x]==0):
				if(board[last_y-2][last_x] + board[last_y-1][last_x] + board[last_y+1][last_x] == 1*stone):
					if(board[last_y+2][last_x] == 0 and board[last_y+3][last_x] == 0):
						if stone == 1:
							for i in range(last_y-2, last_y+2):
								if board[i][last_x] == 0:
									temp.append((last_x, i))
									#board[i][last_x] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_y-2, last_y+2):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x, last_y-2), (last_x, last_y-1), (last_x, last_y+1)])
		if(last_y >= 5 and last_y <= 16):
			if(board[last_y-5][last_x]==0 and board[last_y-4][last_x]==0):
				if(board[last_y-3][last_x] + board[last_y-2][last_x] + board[last_y-1][last_x] == 1*stone):
					if(board[last_y+1][last_x] == 0 and board[last_y+2][last_x] == 0):
						if stone == 1:
							for i in range(last_y-3, last_y+1):
								if board[i][last_x] == 0:
									temp.append((last_x, i))
									#board[i][last_x] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(last_y-3, last_y+1):
								if board[i][last_x] == stone:
									temp.append((last_x, i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x] == 0:
										candidate.add((x, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x, last_y-3), (last_x, last_y-2), (last_x, last_y-1)])
		# \방향
		if(last_x >= 2 and last_x <= 13 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x-2]==0 and board[last_y-1][last_x-1]==0):
				if(board[last_y+1][last_x+1] + board[last_y+2][last_x+2] + board[last_y+3][last_x+3] == 1*stone):
					if(board[last_y+4][last_x+4] == 0 and board[last_y+5][last_x+5] == 0):
						if stone == 1:
							for i in range(0, 4):
								if board[last_y+i][last_x+i] == 0:
									temp.append((last_x+i, last_y+i))
									#board[last_y+i][last_x+i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(0,4):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x+1, last_y+1), (last_x+2, last_y+2), (last_x+3, last_y+3)])
		if(last_x >= 3 and last_x <= 14 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x-3]==0 and board[last_y-2][last_x-2]==0):
				if(board[last_y-1][last_x-1] + board[last_y+1][last_x+1] + board[last_y+2][last_x+2] == 1*stone):
					if(board[last_y+3][last_x+3] == 0 and board[last_y+4][last_x+4] == 0):
						if stone == 1:
							for i in range(-1, 3):
								if board[last_y+i][last_x+i] == 0:
									temp.append((last_x+i, last_y+i))
									#board[last_y+i][last_x+i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(-1, 3):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x-1, last_y-1), (last_x+1, last_y+1), (last_x+2, last_y+2)])
		if(last_x >= 4 and last_x <= 15 and last_y >=4 and last_y <=15):
			if(board[last_y-4][last_x-4]==0 and board[last_y-3][last_x-3]==0):
				if(board[last_y-2][last_x-2] + board[last_y-1][last_x-1] + board[last_y+1][last_x+1] == 1*stone):
					if(board[last_y+2][last_x+2] == 0 and board[last_y+3][last_x+3] == 0):
						if stone == 1:
							for i in range(-2, 2):
								if board[last_y+i][last_x+i] == 0:
									temp.append((last_x+i, last_y+i))
									#board[last_y+i][last_x+i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(-2, 2):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x-2, last_y-2), (last_x-1, last_y-1), (last_x+1, last_y+1)])
		if(last_x >= 5 and last_x <= 16 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x-5]==0 and board[last_y-4][last_x-4]==0):
				if(board[last_y-3][last_x-3] + board[last_y-2][last_x-2] + board[last_y-1][last_x-1] == 1*stone):
					if(board[last_y+1][last_x+1] == 0 and board[last_y+2][last_x+2] == 0):
						if stone == 1:
							for i in range(-3, 1):
								if board[last_y+i][last_x+i] == 0:
									temp.append((last_x+i, last_y+i))
									#board[last_y+i][last_x+i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(-3, 1):
								if board[last_y+i][last_x+i] == stone:
									temp.append((last_x+i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x+j] == 0:
										candidate.add((x+j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x-3, last_y-3), (last_x-2, last_y-2), (last_x-1, last_y-1)])
		# /방향
		if(last_x >= 5 and last_x <= 16 and last_y >=2 and last_y <=13):
			if(board[last_y-2][last_x+2]==0 and board[last_y-1][last_x+1]==0):
				if(board[last_y+1][last_x-1] + board[last_y+2][last_x-2] + board[last_y+3][last_x-3] == 1*stone):
					if(board[last_y+4][last_x-4] == 0 and board[last_y+5][last_x-5] == 0):
						if stone == 1:
							for i in range(0, 4):
								if board[last_y+i][last_x-i] == 0:
									temp.append((last_x-i, last_y+i))
									#board[last_y+i][last_x-i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(0,4):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x-1, last_y+1), (last_x-2, last_y+2), (last_x-3, last_y+3)])
		if(last_x >= 4 and last_x <= 15 and last_y >=3 and last_y <=14):
			if(board[last_y-3][last_x+3]==0 and board[last_y-2][last_x+2]==0):
				if(board[last_y-1][last_x+1] + board[last_y+1][last_x-1] + board[last_y+2][last_x-2] == 1*stone):
					if(board[last_y+3][last_x-3] == 0 and board[last_y+4][last_x-4] == 0):
						if stone == 1:
							for i in range(-1, 3):
								if board[last_y+i][last_x-i] == 0:
									temp.append((last_x-i, last_y+i))
									#board[last_y+i][last_x-i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(-1, 3):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x+1, last_y-1), (last_x-1, last_y+1), (last_x-2, last_y+2)])
		if(last_x >= 4 and last_x <= 14 and last_y >=4 and last_y <=14):
			if(board[last_y-4][last_x+4]==0 and board[last_y-3][last_x+3]==0):
				if(board[last_y-2][last_x+2] + board[last_y-1][last_x+1] + board[last_y+1][last_x-1] == 1*stone):
					if(board[last_y+2][last_x-2] == 0 and board[last_y+3][last_x-3] == 0):
						if stone == 1:
							for i in range(-2, 2):
								if board[last_y+i][last_x-i] == 0:
									temp.append((last_x-i, last_y+i))
									#board[last_y+i][last_x-i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(-2, 2):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x+2, last_y-2), (last_x+1, last_y-1), (last_x-1, last_y+1)])
		if(last_x >= 2 and last_x <= 13 and last_y >=5 and last_y <=16):
			if(board[last_y-5][last_x+5]==0 and board[last_y-4][last_x+4]==0):
				if(board[last_y-3][last_x+3] + board[last_y-2][last_x+2] + board[last_y-1][last_x+1] == 1*stone):
					if(board[last_y+1][last_x-1] == 0 and board[last_y+2][last_x-2] == 0):
						if stone == 1:
							for i in range(-3, 1):
								if board[last_y+i][last_x-i] == 0:
									temp.append((last_x-i, last_y+i))
									#board[last_y+i][last_x-i] = 1
							candidate.add(tuple(temp))
							temp.clear()
						elif stone == 10:
							for i in range(-3, 1):
								if board[last_y+i][last_x-i] == stone:
									temp.append((last_x-i, last_y+i))
							for (x,y) in temp:
								for j in [-2,-1,1,2]:
									if board[y+j][x-j] == 0:
										candidate.add((x-j, y+j))
							temp.clear()
						elif stone == 0:
							candidate.update([(last_x+3, last_y-3), (last_x+2, last_y-2), (last_x+1, last_y-1)])
      
	return candidate