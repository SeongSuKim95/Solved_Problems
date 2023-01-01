from collections import Counter

def solution(topping):
    answer = 0
    topping_dic = Counter(topping)
    set_dic = set()
    for i in topping:
        topping_dic[i] -= 1
        set_dic.add(i)
        if topping_dic[i] == 0 :
            topping_dic.pop(i)
        if len(set_dic) == len(topping_dic.keys()) :
            answer += 1
            
    return answer