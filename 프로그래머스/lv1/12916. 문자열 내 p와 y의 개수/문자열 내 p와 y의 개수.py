def solution(s):
    answer = True
    
    cnt_p,cnt_y = s.lower().count("p"), s.lower().count("y")
    
    return cnt_p == cnt_y
     