from collections import deque

def solution(maps):
    
    answer = 0
    n,m = len(maps),len(maps[0])
    # 상 하 좌 우 
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    q = deque()
    q.append((0,0))
    while q:     
        cur = q.popleft()
        for dir in dirs :
            new_y,new_x = cur[0] + dir[0], cur[1] + dir[1] 
            if 0<= new_y < n and 0<= new_x < m and maps[new_y][new_x] == 1:
                q.append((new_y,new_x))
                maps[new_y][new_x] = maps[cur[0]][cur[1]] + 1
    if maps[n-1][m-1] == 1:
       return -1
    else :
       return maps[n-1][m-1]

    
            