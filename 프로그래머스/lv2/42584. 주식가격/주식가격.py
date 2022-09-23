def solution(prices):
    
    answer = [0] * len(prices)
    stack = []
    
    for i,price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices)- 1- j
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