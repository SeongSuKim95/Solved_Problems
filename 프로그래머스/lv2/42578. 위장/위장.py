import math
from itertools import combinations

def solution(clothes):
    answer = 0
    cloth_dict = {}
    for cloth in clothes :
        if cloth[1] not in cloth_dict.keys():
            cloth_dict[cloth[1]] = 1
        cloth_dict[cloth[1]] += 1
    
    return eval('*'.join([str(n) for n in list(cloth_dict.values())])) - 1
    # for i in range(1,len(cloth_dict.keys())+1):
    #     temp += combinations(cloth_dict.values(),i)
    # for i in temp:
    #     answer += eval('*'.join([str(n) for n in list(i)])) 
    # return answer
    # # if len(cloth_dict.keys()) != 1: 
    #     for value in cloth_dict.values():
    #         temp *= len(value)
    #         answer += len(value)
    #     return answer + temp
    # else:
    #     return len(list(cloth_dict.values())[0])

