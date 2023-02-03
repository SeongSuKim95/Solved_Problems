def solution(s):
    answer = []
    zeros = 0
    cnt = 0
    while s != "1":
        zeros += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt,zeros]