from collections import defaultdict
N = int(input())

_data = [list(map(int,input().split())) for _ in range(N)]

#  0 1 2 3

# 상 --> 좌
# 우 --> 상
# 좌 --> 하
# 하 --> 우

# 우 상 좌 하
_dir = {0 : [1,0], 1 : [0, -1], 2 : [-1,0], 3 : [0,1]}
# 회전시
_coord = defaultdict(int)

for data in _data:
    dir_history = []
    coord_history = []
    x,y,d,g = data
    dir_history.append(d)
    _coord[(x,y)] = 1
    while g:
        for direction in dir_history[::-1]:
            nd = direction + 1
            if nd > 3:
                nd = 0 
            dir_history.append(nd)
        g -= 1
    # print(dir_history)
    for direction in dir_history:
        nx,ny = x + _dir[direction][0], y + _dir[direction][1]
        _coord[(nx,ny)] = 1 
        x,y = nx,ny

_map = [[0] * 101 for _ in range(101)]
for x,y in _coord.keys():
    if 0 <= x <= 100 and 0<= y <= 100:
        _map[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if _map[i][j] and _map[i+1][j] and _map[i][j+1] and _map[i+1][j+1]:
            cnt +=1
print(cnt)


