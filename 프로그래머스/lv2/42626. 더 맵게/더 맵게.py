import heapq

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        answer += 1
    return answer

# def solution(scoville,K):
    
#     answer = 0 
#     heap = []
#     for num in scoville:
#         heapq.heappush(heap,num)
    
#     while heap[0] < K :
#         try:     
#             heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))

#         except IndexError: 
#             return -1 
#         answer += 1
#     return answer