def solution(a, b):
    answer = 0
    for a_list,b_list in zip(a,b):
        answer += a_list*b_list
    return answer