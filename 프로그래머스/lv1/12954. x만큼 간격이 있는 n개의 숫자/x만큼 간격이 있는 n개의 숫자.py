def solution(x, n):
    if x != 0:
        answer = [i for i in range(x,x*n,x)] + [x*n]
    else:
        answer = [x]*n
    return answer