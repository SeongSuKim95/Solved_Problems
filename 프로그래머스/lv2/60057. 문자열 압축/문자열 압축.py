def solution(s):
    cur = 0 
    stack = []
    answer_len = []
    answer_temp = []
    # 5번 테케 : 문자열 길이가 1일때 ex) "a" --> 1
    if len(s) == 1:
        return 1
    for i in range(1,int(len(s)/2)+1): # step
        answer = ''
        for j in range(0,len(s),i): # fragments
            temp = s[j:j+i]
            # print(stack,temp)
            if not stack:
                cnt = 1
                stack.append(temp)
            else:
                if stack[-1] == temp:
                    cnt +=1
                    # print(cnt)
                else :
                    if cnt >= 2:
                        answer += str(cnt) + stack.pop()
                    else:
                        answer += stack.pop()
                    cnt = 1
                    stack.append(temp)
        if cnt != 1:
            answer += str(cnt) + stack.pop()
        else:
            answer += stack.pop()
        answer_len.append(len(answer))
    return min(answer_len)


            
        
        