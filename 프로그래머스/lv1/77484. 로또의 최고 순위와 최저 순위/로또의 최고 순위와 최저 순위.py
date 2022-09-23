def solution(lottos, win_nums):
    dict = { 6:1, 5:2, 4:3, 3:4, 2:5 , 1:6 , 0:6 }
    temp = [item for item in lottos if item != 0]
    min = len(list(set(temp) & set(win_nums)))
    
    max = lottos.count(0) + min
    
    answer = [dict[max], dict[min]]
    return answer