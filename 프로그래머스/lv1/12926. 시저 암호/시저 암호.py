def solution(s, n):
    answer = ''
    # 97 --> 122
    # 65 --> 90
    for i in s :
        temp = ord(i) + n 
        if i.isupper():
            if temp > 90:
                temp -= 26
            answer += chr(temp)
        elif i.islower():
            if temp > 122 :
                temp -= 26
            answer += chr(temp)
        else:
            answer += " "
    return answer