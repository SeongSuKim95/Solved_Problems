from collections import deque

answer = 0
def dfs(numbers,target,sum,idx):
    global answer
    if idx == len(numbers):
        if sum == target:
            answer +=1
    else:
        cur = numbers[idx]
        dfs(numbers,target,sum+cur,idx+1)
        dfs(numbers,target,sum-cur,idx+1)
        
    
def solution(numbers,target):
    idx = 0
    dfs(numbers,target,0,idx)
    
    return answer
