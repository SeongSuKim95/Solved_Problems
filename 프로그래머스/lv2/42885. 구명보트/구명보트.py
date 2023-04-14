def solution(people, limit):
    result = 0
    
    people.sort()
    
    minp, maxp = 0,len(people) - 1
    
    while minp < maxp :
        if people[minp] + people[maxp] > limit:
            maxp -= 1
        else :
            minp += 1
            maxp -= 1
        result += 1
    if minp == maxp :
        result += 1
    return result
