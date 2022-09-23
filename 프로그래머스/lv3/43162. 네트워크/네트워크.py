from collections import deque, defaultdict

# def DFS(computers,com,visited):
    
#     visited[com] = True
    
#     for idx,connect in enumerate(computers[com]):
#         if connect and visited[idx] == False:
#             DFS(computers,idx,visited)

# def BFS(n,computers,com,visited):
    
#     visited[com] = True
#     queue = deque([com])

#     while queue:
#         com = queue.popleft()
#         visited[com] = True
#         for connect in range(n):
#             if connect != com and computers[com][connect]:
#                 if visited[connect]== False:
#                     queue.append(connect)
  
def DFS(n,computer,com,visited):
    
    visited[com] = True
    
    for idx,connect in enumerate(computer[com]):
        if visited[idx] == False and connect:
            DFS(n,computer,idx,visited)
    
# def BFS(n,computers,com,visited):
    
#     visited[com] = True
#     queue = deque([com])
    
#     while queue:
#         cur = queue.popleft()
#         for idx, connect in enumerate(computers[cur]):
#             if connect and visited[idx] == False:
#                 queue.append(idx)
#                 visited[idx] = True
    

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for com in range(n): # 이를 위해 for com in range(n)과 같이 모든 컴퓨터에 대해서 loop를 돌아야 한다.
        if visited[com] == False:
            DFS(n,computers,com,visited)
            # DFS든 BFS든 재귀, loop를 마치고 돌아온다면 하나의 묶음을 탐색한 것이므로 answer에 1을 더해준다.
            answer +=1
    
    return answer

        
        
