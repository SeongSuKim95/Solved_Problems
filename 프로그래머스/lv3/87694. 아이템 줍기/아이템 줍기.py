from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 상 하 좌 우
    # 
    dirs = [(0,-1),(0,1),(-1,0),(1,0)]
    MAX_SIZE = 51
    map_ = [[-1] * MAX_SIZE * 2  for _ in range(MAX_SIZE * 2)] # 2를 곱해주는 이유는??
    
    for coords in rectangle :
        x1,y1,x2,y2 = map(lambda x : x*2, coords)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2 :
                    map_[i][j] = 0
                elif map_[i][j] != 0 :
                    map_[i][j] = 1
                    
    q = deque()
    q.append((characterX * 2 ,characterY * 2))
    visited = [[False] * MAX_SIZE * 2 for i in range(MAX_SIZE *2)]
    while q:
        cur = q.popleft()
        for dir in dirs :
            nx, ny = cur[0] + dir[0], cur[1] + dir[1]
            if 0<= ny < MAX_SIZE * 2 and 0<= nx < MAX_SIZE * 2 and map_[nx][ny] == 1 and not visited[nx][ny] :
                map_[nx][ny] = map_[cur[0]][cur[1]] + 1
                q.append((nx,ny))
                if ny == itemY * 2  and nx == itemX * 2 :
                    answer = map_[nx][ny]//2
                    break
            

    return answer