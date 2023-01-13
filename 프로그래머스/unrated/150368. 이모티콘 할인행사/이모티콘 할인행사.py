from itertools import product

def solution(users, emoticons):
    answer = []
    # 할인율 : 10,20,30,40
    # 이모티콘 정보 : max 7개, 100만원
    
    # 1. 할인율 별로 emoticon 가격 책정 list 
    sale_rate = [10,20,30,40]
    answer_person, answer_pay = 0,0
    for combi in product(sale_rate,repeat=len(emoticons)):
        num_person, sum_pay = 0,0
        for user in users : # 각 combi에 대해 user들의 행동
            user_min_sale, user_max_pay = user[0],user[1]    
            user_sum_pay = 0
            for idx, i in enumerate(combi) :
                if i >= user_min_sale: # 할인율이 user기준보다 높으면
                    user_sum_pay += (100-i)/100 * emoticons[idx]
            if user_sum_pay >= user_max_pay :
                num_person += 1
                user_sum_pay = 0
            sum_pay += user_sum_pay
        
        if num_person > answer_person :
            answer_person,answer_pay = num_person,sum_pay
        elif num_person == answer_person : 
            if sum_pay > answer_pay:
                answer_pay = sum_pay
            
    return [answer_person,answer_pay]