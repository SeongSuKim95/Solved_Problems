# def solution(s):
#     answer = ''
#     a = s.split(' ')
    
#     for idx, i in enumerate(a):
#         temp = i.lower()
#         temp = temp[0].upper() + temp[1:]
#         answer += temp + ' ' 
#     return answer[:-1]
def solution(s):
    
    answer = ''
    flag = True
    answer = []
    for i in s:
        
        if i == ' ':
            flag = True
            answer.append(i)
        else : 
            if flag == True:
                answer.append(i.upper())
                flag = False
            else :
                if i.isalpha():
                    answer.append(i.lower())
    
    return ''.join(answer)
        
        