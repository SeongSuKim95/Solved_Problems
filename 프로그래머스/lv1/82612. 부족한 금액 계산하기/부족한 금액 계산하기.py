def solution(price, money, count):
    
    price_sum =price * count * (count+1)/ 2
    if price_sum <= money:
        return 0
    else:
        return price_sum - money
    