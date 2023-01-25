def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n # 몫
        b = i%n #나머지 
        if a<b: a,b =b,a #큰거 구하기 
        answer.append(a+1)
    
    return answer
    
    
#        1   2   3
# #     0,1 0,2 1,0
#        4   5   6
# #     1,1 1,2 2,0
#        7   8   9
# #     2,1 2,2 3,0
