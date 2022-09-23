def solution(s):
    answer = ''
    word_list = s.split(' ')
    
    for word in word_list:
        word = word.lower()
        temp = ''
        for idx,alpha in enumerate(word):
            if idx % 2 == 0 :
                temp += alpha.upper()
            else:
                temp += alpha
        answer += temp + ' '
    return answer[:-1]