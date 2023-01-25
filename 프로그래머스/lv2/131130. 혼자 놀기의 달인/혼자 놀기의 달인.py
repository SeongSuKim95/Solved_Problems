def solution(cards):
    answer = 0
    data = {num : index+1 for index, num in enumerate(cards)}
    
    for card in cards:
        data_ = data.copy()
        card_ = card
        cnt_1 = 0
        while data_[card_]:
            temp = data_[card_]
            data_[card_] = 0
            card_ = temp 
            cnt_1 += 1
        for card2,v in data_.items():
            if v :
                data_2 = data_.copy()
                card_2 = card2
                cnt_2 = 0
                while data_2[card_2] :
                    temp = data_2[card_2]
                    data_2[card_2] = 0
                    card_2 = temp
                    cnt_2 += 1
                answer = max(answer,cnt_1*cnt_2)    
        
    
    return answer