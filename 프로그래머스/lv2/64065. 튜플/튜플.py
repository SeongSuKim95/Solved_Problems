def solution(s):
    temp = s[2:-2].split("},{")

    temp.sort(key=lambda x : len(x))

    answer = []
    set_dict = {}
    for i in temp:
        b = list(map(int,i.split(",")))
        for j in b:
            try:
                if set_dict[j]:
                    continue
            except:
                set_dict[j] = True
                answer.append(j)
    return answer