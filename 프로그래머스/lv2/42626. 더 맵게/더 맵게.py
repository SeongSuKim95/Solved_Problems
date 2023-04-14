import heapq

def solution(scoville,K):
    answer = 0
    pq = []
    
    for food in scoville:
        heapq.heappush(pq,food)
    
    while pq[0] < K and len(pq) >= 2:
        
        s1 = heapq.heappop(pq)
        s2 = heapq.heappop(pq)
        new_s = s1 + 2*s2
        heapq.heappush(pq,new_s)
        answer += 1
    
    if pq[0] < K :
        return -1
    
    return answer
