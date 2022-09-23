# def solution(n):
#     answer = 0
#     num_list = {i:0 for i in range(1,n+1)}
    
#     for i in range(1,n+1):
#         for j in range(i,n+1,i):
#             num_list[j] +=1
    
#     answer = list(num_list.values()).count(2)
#     return answer

def solution(n):
    num = set(range(2,n+1))

    for i in range(2,int(n**0.5)+1):
        if i in num:
            num-=set(range(i**2,n+1,i))
    return len(num)