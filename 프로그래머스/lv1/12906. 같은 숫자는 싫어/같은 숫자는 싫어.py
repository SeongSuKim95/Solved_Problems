def solution(arr):
    
    stack = []
    
    for i in range(len(arr)):
        
        if not stack:
            stack.append(arr[i])
        else:
            if stack[-1] != arr[i]:
                stack.append(arr[i])

    return stack