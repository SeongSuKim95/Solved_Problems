def solution(n):
    answer = 0
    
    ones = bin(n).count('1')
    
    while True:
        n += 1
        if ones == bin(n).count('1'):
            return n
   