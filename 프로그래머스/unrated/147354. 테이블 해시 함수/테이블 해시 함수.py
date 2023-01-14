def solution(data, col, row_begin, row_end):
    answer = 0 
    sorted_data = sorted(data,key = lambda x : [x[col-1],-x[0]]) # 중요도 순으로 정렬
    for i in range(row_begin-1,row_end):
        answer ^= sum([j%(i+1) for j in sorted_data[i]])
    
    return answer