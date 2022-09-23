def solution(arr1, arr2):
    answer = []
    
    for a,b in zip(arr1,arr2):
        temp = []
        for c,d in zip(a,b):
            temp.append(c+d)
        answer.append(temp)
    return answer