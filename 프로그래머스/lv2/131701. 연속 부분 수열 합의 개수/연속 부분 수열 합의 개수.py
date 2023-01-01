def solution(elements):
    answer = {}
    for i in elements :
        answer[i] = True
    answer[sum(elements)] = True
    elements_c = elements + elements[:-1]
    length = len(elements)
    
    for i in range(2,length):
        for j in range(length):
            answer[sum(elements_c[j:j+i])] = True
    
    return len(answer.keys())
    

# 7 9 1 1 4 7 9 1 1 