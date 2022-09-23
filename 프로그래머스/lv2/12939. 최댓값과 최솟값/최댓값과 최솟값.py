def solution(s):
    answer = ''
    num_list = s.split(' ')
    num_list = [int(i) for i in num_list]

    return str(min(num_list))+' '+str(max(num_list))