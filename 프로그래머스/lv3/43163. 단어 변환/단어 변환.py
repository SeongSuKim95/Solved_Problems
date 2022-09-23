
from collections import deque
answer = []
def dfs(begin,data,target,depth,words,visited):
    global answer

    visited[begin] = True
    for i in data[begin]:
        if visited[i] == False and words[i] != target:
            dfs(i,data,target,depth+1,words,visited)
        elif visited[i] == False and words[i] == target:
            answer.append(depth)
    
def solution(begin, target, words):
    
    words = [begin] + words
    data = [[] for _ in words]
    
    for idx_1,i in enumerate(words):
        for idx_2,j in enumerate(words):
            temp = 0
            for k in range(len(i)):
                if i[k] != j[k] :
                    temp +=1
            if temp == 1:
                data[idx_1].append(idx_2)
                
    visited = [False] * len(words)
    if target in words:    
        dfs(0,data,target,1,words,visited)
        if answer :
            return min(answer)
        else:
            return 0
    else:
        return 0
    



