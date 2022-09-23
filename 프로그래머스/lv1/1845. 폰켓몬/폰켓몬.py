

def solution(nums):
    num_set = list(set(nums))
    
    return min(len(num_set),len(nums)/2) 