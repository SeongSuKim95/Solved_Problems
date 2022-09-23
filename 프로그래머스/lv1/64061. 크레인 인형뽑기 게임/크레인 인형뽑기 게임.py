def solution(board, moves):
    answer = 0
    temp = []
    zero_count = []
    stack = []
    size = len(board[0])
    for j in range(size):
        temp.append([i[j] for i in board])
    
    for i in temp:
        zero_count.append(i.count(0))
    cnt = 0
    if moves:
        for idx,k in enumerate(moves):
            if zero_count[k-1] >= size :
                pass
            else : 
                stack.append(temp[k-1][zero_count[k-1]])
                zero_count[k-1] = zero_count[k-1] + 1

            while len(stack)>= 2 and stack[-2] == stack[-1] :
                stack.pop()
                stack.pop()
                cnt +=2

    return cnt