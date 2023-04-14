import heapq

def solution(operations):
    
    min_heap, max_heap = [], []
    for operation in operations :
        
        op, num = operation.split()
        
        if op == "I":
            heapq.heappush(min_heap,int(num))
            heapq.heappush(max_heap,-int(num))
        else :
            if num == "1": # max값 제거
                if max_heap :
                    max_num = -heapq.heappop(max_heap)
                    min_heap.remove(max_num)
            else :
                if min_heap :
                    min_num = heapq.heappop(min_heap)
                    max_heap.remove(-min_num)
    if min_heap :
        return (-heapq.heappop(max_heap),heapq.heappop(min_heap))
    else :
        return [0,0]
        