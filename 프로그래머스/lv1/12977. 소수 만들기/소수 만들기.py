from itertools import combinations


def solution(nums):
    answer = 0
    for i in list(combinations(nums,3)):
        cnt = 0
        sum_num = sum(i)
        for j in range(sum_num-1,1,-1):
            if sum_num % j == 0 :
                cnt = 1
                break
        if cnt != 1:
            answer+=1
        
    return answer