def solution(s):
    
    stack = []
    for elem in s :
        if not stack:
            stack.append(elem)
        else:
            if stack[-1] == "(" and elem ==")":
                stack.pop()
            else :
                stack.append(elem)
    if stack:
        return False
    else:
        return True