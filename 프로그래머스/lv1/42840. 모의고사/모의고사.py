def solution(answers):
    answer = 0
    # dict = {1: 0, 2: 0, 3: 0}
    # temp1 = [1,3,4,5]
    # temp2 = [3,1,2,4,5]
    # for idx, num in enumerate(answers):
    #     if num == idx % 5 or num % 5 == 0:
    #         dict[1] +=1
    #     if idx % 2 == 0 and num == 2:
    #         dict[2] +=1
    #     elif idx % 2 !=0:
    #         if temp1[int(idx/2) % 4 - 1] == num :
    #             dict[2] +=1
    #     if temp2[int(idx/ 2) % 5 -1] == num:
    #         dict[3] +=1
    # print(dict)
    
    answer_num = {1:0,2:0,3:0}
    seq1 = [1,2,3,4,5]
    seq2 = [1,3,4,5]
    seq3 = [3,1,2,4,5]
    for idx,num in enumerate(answers):
        if (num % 6) == seq1[idx % 5] :
            answer_num[1] +=1
        if (idx % 2) == 0 and num == 2 :
            answer_num[2] +=1
        elif (idx % 2) == 1 and num == seq2[int(idx/2) % 4]:
            answer_num[2] +=1
        if seq3[int(idx/2) % 5] == num:
            answer_num[3] +=1
    
    answer = sorted([k for k,v in answer_num.items() if max(answer_num.values()) == v])
    
    #answer = max(answer_num,key=answer_num.get)
    return answer