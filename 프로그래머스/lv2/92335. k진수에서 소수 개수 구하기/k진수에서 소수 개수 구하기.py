# import re 
# def change(n,k):
     
#     answer = ''
#     while n // k :
#         n_div = n // k
#         n_mod = n % k
#         answer += str(n_mod)
#         if n_div < k :  
#             answer += str(n_div)
#         n = n_div    
#     return answer[::-1]


# def solution(n, k):
#     answer = -1
    
#     changed = change(n,k)
#     print(changed)
#     p = re.compile('0?\d+0?')
#     print(re.findall(p,changed))
#     return answer
def is_prime(number):
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return False if number == 1 else True
    
def solution(n, k):
    answer = 0
    str_n = ''
    while n > 0:
        str_n = str(n % k) + str_n
        n //= k
    
    for num in str_n.split('0'):
        if num == '':
            continue
        if is_prime(int(num)):
            answer += 1
    
    return answer