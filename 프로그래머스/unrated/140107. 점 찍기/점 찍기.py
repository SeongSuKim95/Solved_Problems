def solution(k, d):
    
    answer = 0
    
    start_y = d - d % k
    start_x = 0 
    debug = []
    while start_y >= 0 :
        if (start_y ** 2 +  start_x ** 2) <= d**2:
            answer += (start_y // k) + 1 
            start_x += k
        else : 
            start_y -= k 
    return answer