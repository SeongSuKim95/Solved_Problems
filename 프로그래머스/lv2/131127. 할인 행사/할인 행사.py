def solution(want, number, discount):
    answer = 0
    num_dict = {}
    
    for w,num in zip(want,number):
        num_dict[w] =num
    
    for i in range(len(discount)-9):
        temp = num_dict.copy()
        for j in discount[i:i+10]:
            if j not in temp.keys():
                break
            else :
                temp[j] -= 1
                if temp[j] == 0 :
                    temp.pop(j)
        if not temp : answer +=1
    return answer