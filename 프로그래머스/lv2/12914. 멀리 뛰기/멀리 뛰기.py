def solution(n):
    a1 = 1
    a2 = 2
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    else :
        for i in range(n-2):
            temp1 = a1 
            temp2 = a2 
            a1 = temp2 
            a2 = temp1 + temp2 
    return a2 % 1234567