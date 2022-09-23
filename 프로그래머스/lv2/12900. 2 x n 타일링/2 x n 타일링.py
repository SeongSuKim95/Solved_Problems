# def tile(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return tile(n-1)+tile(n-2)
    
def solution(n):
    
    a1 = 1
    a2 = 2
    if n == 1:
        return a1
    elif n == 2:
        return a2
    else:
        for i in range(2,n):
            a1,a2 = a2,a1+a2
    return a2 % 1000000007

