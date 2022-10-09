N = int(input())

_data = [list(map(int,input().split())) for _ in range(N**2)]

_data_dict = {}
for datas in _data:
    _data_dict[datas[0]] = datas[1:]


_map = [[0]*(N+1) for _ in range(N+1)]

# 상 하 좌 우 
_dirlist = [[-1,0],[1,0],[0,-1],[0,1]]
FLAG = False
for cur_student,friends in _data_dict.items():
    
    # 첫 자리는 그냥 놓자!
    if not FLAG:
        _map[2][2] = cur_student
        FLAG = True
        continue

    coord_info = {}
    for row in range(1,N+1):
        for col in range(1,N+1):
            # 빈 자리에 대해서
            if _map[row][col] == 0:
                friends_cnt = 0
                empty_cnt = 0   
                for dir in _dirlist:
                   nrow = row + dir[0] 
                   ncol = col + dir[1]
                   if 1<= nrow <= N and 1<= ncol <= N:
                        if _map[nrow][ncol] in friends:
                            friends_cnt += 1
                        if _map[nrow][ncol] == 0:
                            empty_cnt += 1
                   else:
                        continue
                coord_info[(row,col)] = (friends_cnt,empty_cnt)
    
    coord_info = sorted(coord_info.items(), key = lambda x : x[1], reverse = True)
    _map[coord_info[0][0][0]][coord_info[0][0][1]] = cur_student

score = 0
score_list = {0:0,1:1,2:10,3:100,4:1000}

for row in range(1,N+1):
    for col in range(1,N+1):
        cnt = 0 
        friends = _data_dict[_map[row][col]]
        for dir in _dirlist:
            nrow = row + dir[0] 
            ncol = col + dir[1]
            if 1<= nrow <= N and 1<= ncol <= N:
                if _map[nrow][ncol] in friends:
                        cnt += 1
        score += score_list[cnt]       
print(score)