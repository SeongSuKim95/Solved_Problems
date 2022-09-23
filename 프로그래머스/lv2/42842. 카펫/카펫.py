def solution(brown, yellow):
    answer = []
    s = brown + yellow
    
    for i in range(1,int(s**(1/2))+1):
        if s % i == 0 :
            if brown == 2 * ( i + s//i + -2) :
                if i >= s//i :
                    return [i,s//i]
                else :
                    return [s//i,i]