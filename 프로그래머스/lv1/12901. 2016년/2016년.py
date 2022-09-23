def solution(a, b):
    answer = ''
    
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    answer = day[(sum(date[:a-1])+b-1)%7]
    
    return answer