
from collections import deque

answer = 100
def dfs(index, depth, maps, target, words, visited):
    global answer
    if words[index] == target:
        answer = min(answer,depth)
    else :
        for i in maps[index]:
            if not visited[i]: 
                visited[i] = True
                dfs(i,depth+1,maps,target,words,visited)
                visited[i] = False

def solution(begin, target, words):
    if target not in words :
        return 0
    words = [begin] + words
    maps = {i : [] for i in range(len(words))}
    for idx1,word1 in enumerate(words) :
        for idx2,word2 in enumerate(words):
            if idx1 < idx2 :
                cnt = 0 
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        cnt += 1
                if cnt == 1:
                    maps[idx1].append(idx2)
                    maps[idx2].append(idx1)
    
    visited = [False] * len(words)
    visited[0] = True
    dfs(0,0,maps,target,words,visited)
    return answer        

# 최단거리이므로 bfs로 푸는게 효율적!


