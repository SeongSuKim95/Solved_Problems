from collections import defaultdict, deque
# def solution(phone_book):
#     answer = True
    
#     phone_book.sort(key=lambda x : len(x))
    
#     queue = deque(phone_book)
    
#     while queue:
#         cur = queue.popleft()
#         for i in queue:
#             if cur == i[:len(cur)]:
#                 answer = False
#     return answer

def solution(phone_book):
    
    answer = True
    phone_book.sort(key=lambda x : len(x))
    
    max_len,min_len = len(phone_book[-1]),len(phone_book[0])
  
    for i in range(min_len,max_len+1):
        temp = defaultdict(int)
        for j in phone_book:
            if temp[j[:i]] :
                return False
            else:
                if len(j) == i:
                    temp[j[:i]] = 1

    return answer