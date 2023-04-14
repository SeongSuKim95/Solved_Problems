def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    
    costs.sort(key=lambda x : x[2])

    def union(a,b):

        a, b= find_parent(a),find_parent(b)

        if a > b :
            parent[a] = b
        else :
            parent[b] = a
            
    def find_parent(x):

        if parent[x] != x :
            parent[x] = find_parent(parent[x])
        return parent[x]


    for a,b,cost in costs:
        if find_parent(a) != find_parent(b):
            union(a,b)
            answer += cost
    
    return answer