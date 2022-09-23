def solution(arr):
    answer = 1
    for i in arr:
        answer = lcm(answer,i)
    return answer

def lcm(a,b):
    answer = 1
    for i in range(1,max(a,b)):
        if a % i == 0 and b % i == 0 and i >= answer:
            answer = i
    
    return answer * a//answer * b//answer

# def solution(arr):
#     cnt = 0
#     lcm = 0
#     lcm_list = []
#     answer = 0
#     while lcm != 1:
#         for i in range(1,max(arr)+1):
#             cnt = 0
#             for j in arr :
#                 if j%i != 0:
#                     cnt = 0
#                     break
#                 else:
#                     cnt +=1
#             if cnt == len(arr) and i > lcm :
#                 lcm = i
#         if lcm != 1:
#             lcm_list.append(lcm)
#             for idx, num in enumerate(arr):
#                 arr[idx] = num//lcm
#             lcm = 0 
#     print(arr,lcm_list)
#     return answer