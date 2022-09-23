def solution(s):
    
    dict = {"zero": "0","one": "1" ,"two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    for num_str in dict.keys():
        if num_str in s :
            s = s.replace(num_str,dict[num_str])
    
    return int(s)