def solution(num):
    
    answer = 0
    while answer < 500:
        if num ==1 :
            return 0
        answer +=1
        if num % 2 == 0:
            num /= 2
        else :
            num = num*3 + 1
        if num == 1:
             return answer
            
    return -1
        
    
   