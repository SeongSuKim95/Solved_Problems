import math
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        temp = math.sqrt(i)
        if temp == int(temp):
            answer -= i
        else :
            answer += i
    return answer