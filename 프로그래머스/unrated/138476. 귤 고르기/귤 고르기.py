from collections import Counter
def solution(k, tangerine):
    answer = 0
    for key,value in  sorted(Counter(tangerine).items(),key=lambda x : x[1],reverse=True):
        k -= value
        answer +=1
        if k <= 0 :
            return answer