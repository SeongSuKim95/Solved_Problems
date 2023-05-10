from collections import deque

N, M = list(map(int,input().split()))

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    datas = list(map(int,input().split()))
    num, singers = datas[0], datas[1:]
    for i in range(num-1):
        graph[singers[i]].append(singers[i+1])
        indegree[singers[i+1]] += 1

q = deque()
for i in range(1,N+1):
    if indegree[i] == 0 :
        q.append(i)
result = []
while q :
    cur = q.popleft()
    result.append(cur)
    for elem in graph[cur]:
        indegree[elem] -= 1
        if indegree[elem] == 0:
            q.append(elem)

if len(result) != N :
    print(0)
else:
    for i in result:
        print(i)
