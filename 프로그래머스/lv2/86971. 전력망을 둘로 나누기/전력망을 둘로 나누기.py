from collections import deque

def solution(n,wires):
    
    answer = 1e9
    for i in range(len(wires)):
        temp_wires = [wire[:] for wire in wires]
        temp_wires.pop(i)
        
        graph = [[] for _ in range(n+1)]
    
        for a,b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False for _ in range(n+1)]
        
        q = deque()
        visited[temp_wires[0][0]] = True
        q.append(temp_wires[0][0])
        
        while q :
            cur_node = q.popleft()
            for adj_node in graph[cur_node]:
                if not visited[adj_node] :
                    visited[adj_node] = True
                    q.append(adj_node)
        
        answer = min(answer,abs((n-sum(visited)) - sum(visited)))
        
    return answer