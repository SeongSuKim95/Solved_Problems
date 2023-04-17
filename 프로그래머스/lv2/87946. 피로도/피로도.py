answer = -1e9

def dfs(k,cnt,dungeons,visited):
    global answer
    if cnt == len(dungeons) or len(dungeons) - cnt + sum(visited) <= answer:
        answer = max(answer,sum(visited))
        return
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0] :
            visited[i] = True
            dfs(k-dungeons[i][1],cnt+1,dungeons,visited)
            visited[i] = False
            
            dfs(k,cnt+1,dungeons,visited)
        
def solution(k, dungeons):
    
    global answer
    
    visited = [False] * len(dungeons)
    
    dfs(k,0,dungeons,visited)
    
    return answer