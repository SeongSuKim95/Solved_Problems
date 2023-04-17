def solution(prices):
    
    answer = [0] * len(prices)
    stack = []
    
    for idx,price in enumerate(prices):
        while stack and prices[stack[-1]] > price :
            prev = stack.pop() 
            answer[prev] = idx - prev
        stack.append(idx)
    
    while stack :
        prev = stack.pop()
        answer[prev] = idx - prev 
        
    return answer

#     answer = []
    
#     while prices:
#         cnt= 0
#         price = prices.pop(0)
#         for p in prices:
#             cnt +=1
#             if p < price:
#                 break
        
#         answer.append(cnt)
        
#     return answer