cnt = 0

def dfs(numbers,target,depth,sum):
    global cnt
    if depth == len(numbers):
        if sum == target:
            cnt += 1
    else :
        num = numbers[depth]
        dfs(numbers,target,depth+1,sum-num)
        dfs(numbers,target,depth+1,sum+num)
    
def solution(numbers,target):
    
    sum = 0
    dfs(numbers,target,0,sum)
    
    return cnt
