import heapq
def solution(priorities, location):
    
    answer = []
    wait_list = []
    pq = []
    
    for idx,elem in enumerate(priorities):
        wait_list.append((idx,elem))
        heapq.heappush(pq,-elem)
    cnt = 0
    
    while wait_list :
        if wait_list[0][1] == -pq[0]:
            idx,v = wait_list.pop(0)
            heapq.heappop(pq)
            cnt += 1
            if idx == location :
                return cnt
        else :
            idx,v = wait_list.pop(0)
            wait_list.append((idx,v))