from collections import deque

def solution(progresses, speeds):
    
    # 앞에 기능이 전부 100이 되어야 True
    # 매주 몇개의 기능이 배포되는가?
    answer = []
    q_progress = deque(progresses)
    q_speed = deque(speeds)
    while q_progress:
        # 개발 진행
        for i in range(len(q_progress)):
            q_progress[i] += q_speed[i]
        cnt = 0
        
        while q_progress and q_progress[0] >= 100: # queue의 경우 앞에서부터 보면서 조건 맞으면 popleft
            # stack의 경우 뒤에서 부터 보면서 조건 맞으면 pop
            q_progress.popleft() # 맨 앞
            q_speed.popleft()
            cnt +=1
        if cnt > 0 :
            answer.append(cnt)
    return answer