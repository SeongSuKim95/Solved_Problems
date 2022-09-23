def solution(participant, completion):

    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
    return list(key for key, val in d.items() if val == 1)[0]