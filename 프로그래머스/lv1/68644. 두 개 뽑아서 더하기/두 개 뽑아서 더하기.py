

def solution(numbers):
    answer = []

    for idx,i in enumerate(numbers):
        for j in numbers[idx+1:]:
            if idx < len(numbers)-1:
                answer.append(i+j)
    return sorted(list(set(answer)))