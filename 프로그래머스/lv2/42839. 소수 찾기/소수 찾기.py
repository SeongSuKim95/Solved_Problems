from itertools import permutations as pm
def solution(numbers):
    answer = 0
    data = []
    for i in range(1,len(numbers)+1):
        for comb in list(pm(numbers,i)):
            temp = int(''.join(comb))
            if temp > 1:
                data.append(temp)
    
    data = list(set(data))
    
    for i in data:
        for j in range(2,int(i**(1/2))+1):
            temp = i / j
            if temp == int(temp):
                answer +=1
                break

    return len(data) - answer