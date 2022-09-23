def solution(strings, n):
    answer = sorted(sorted(strings),key= lambda key : key[n])    
    return answer