from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)
    for connection in computers : 
        for computer,connect in enumerate(connection) :
            if connect and not visited[computer]:
                q = deque()
                q.append(computer)
                while q :
                    cur = q.popleft()
                    visited[cur] = True
                    for idx,i in enumerate(computers[cur]):
                        if i and not visited[idx]:
                            q.append(idx)
                answer += 1        
    
    return answer

        
        
