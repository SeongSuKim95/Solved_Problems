def solution(s):

    answer = ''
    stack = []
    for i in s:
        if not stack :
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if stack :
        return 0
    else:
        return 1 
