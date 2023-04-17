## Back tracking을 이용한 풀이

answer = 0
N = 0
visited =[]
def dfs(k,cnt,dungeons):
    global answer
    
    if cnt > answer:
        answer = cnt

    for i in range(N):
        if k >=dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k-dungeons[i][1],cnt+1,dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global N,visited    
    N = len(dungeons)
    visited = [0] * N
    dfs(k,0,dungeons)
        
    return answer