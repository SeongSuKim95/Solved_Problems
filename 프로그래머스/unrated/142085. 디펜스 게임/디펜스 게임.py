# 첫 풀이    
#     if k >= len(enemy) : return len(enemy)    
    
#     for i in range(k+1,len(enemy)+1):
#         temp = enemy[:i]
#         k_max = sum(sorted(temp,reverse=True)[:k])
#         if sum(temp)- k_max > n :
#             return i-1

# 두번째 풀이

#     if k >= len(enemy) : return len(enemy)
#     idx, cnt = 0 , 0
#     while cnt <= k and n >= 0:
#         n -= enemy[idx]
#         if n < 0 :
#             n += sorted(enemy[:idx+1],reverse=True)[cnt]
#             cnt += 1
#         idx += 1
#     return idx - 1

# 정답

from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy: # -부호 붙여서 최대힙으로 변환
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0: break
            sumEnemy += heappop(heap) 
            k -= 1
        answer += 1
    return answer