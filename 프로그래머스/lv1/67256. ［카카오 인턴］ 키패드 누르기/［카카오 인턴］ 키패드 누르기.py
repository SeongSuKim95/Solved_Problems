import math
def solution(numbers, hand):
    answer = ''
    map = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2], 0: [3,1]}
    group = {(1,4,7): "L", (2,5,8,0): "M", (3,6,9): "R"}
    stack = {"L":[],"R":[],"M":[]}
    for i, num in enumerate(numbers):    
        for num_group in group:
            if num in num_group:
                side  = group[num_group]
                if side == "L" or side == "R":
                    stack[side].append(num)
                    answer += side
                else :
                    cur_pix = map[num]
                    if stack["L"]:
                        L_pix = map[stack["L"][-1]]
                    else :
                        L_pix = [3,0]
                    if stack["R"]:
                        R_pix = map[stack["R"][-1]]
                    else :
                        R_pix = [3,2]
                        
                    cur_L = math.ceil(math.sqrt((cur_pix[0] - L_pix[0])**2 + (cur_pix[1] - L_pix[1])**2))
                    cur_R = math.ceil(math.sqrt((cur_pix[0] - R_pix[0])**2 + (cur_pix[1] - R_pix[1])**2))
                    
                    if cur_L > cur_R:
                        side = "R"
                    elif cur_L < cur_R:
                        side = "L"
                    elif cur_L == cur_R:
                        side = hand[0].upper()
                    stack[side].append(num)
                    answer += side
    return answer