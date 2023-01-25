from collections import defaultdict
def solution(dirs):
    answer = 0
    
    dir_list = {"U":(0,1),"L":(-1,0),"D":(0,-1),"R":(1,0)}
    cur = (0,0)
    history = defaultdict(list)
    for dir in dirs :
        new = (cur[0] + dir_list[dir][0], cur[1] + dir_list[dir][1])
        if new[0] > 5 or new[0] < -5 or new[1] > 5 or new[1] <-5 :
            continue
        if not history[cur] or (new not in history[cur]):
            history[cur].append(new)
            history[new].append(cur)
            answer +=1
        cur = new
    return answer