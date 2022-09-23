def solution(priorities, location):
    answer = []
    index = [i for i in range(len(priorities))]
    while priorities:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            answer.append(index.pop(0))
        else:
            priorities.append(priorities.pop(0))
            index.append(index.pop(0))
    
    return answer.index(location)+1