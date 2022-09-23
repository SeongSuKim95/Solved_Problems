def solution(operations):
    answer = []
    
    for i in operations:
        op,num = i.split(" ")
        if op == "I" :
            answer.append(int(num))
        else:
            if answer:
                if num == "1":
                    answer.remove(max(answer))
                elif num == "-1":
                    answer.remove(min(answer))
    if not answer:
        answer = [0,0]
    else:
        answer = [max(answer),min(answer)]
    return answer
