N = int(input())

first,end = input().split("*")

def simulate(cur_string):
    if len(first) + len(end) > len(cur_string):
        print("NE")
        return
    
    if cur_string[:len(first)] == first and cur_string[-len(end):] == end :
        print("DA")
        return
    else :
        print("NE")
        return

for _ in range(N):
    simulate(input())
            