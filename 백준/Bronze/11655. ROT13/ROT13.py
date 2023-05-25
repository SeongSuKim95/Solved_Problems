string = input()

a , z = ord("a"), ord("z")
A , Z = ord("A"), ord("Z")
len_s = z - a + 1
len_l = Z - A + 1
answer = ""
# print(ord("a"),ord("z"),ord("A"),ord("Z"))
for i in string :
    cur = ord(i)
    if a <= cur and cur <= z :
        cur -= a
        idx = (cur + 13 + len_s) % len_s
        idx += a
        answer += chr(idx)
    elif A <= cur and cur <= Z:
        cur -= A
        idx = (cur + 13 + len_l) % len_l
        idx += A
        answer += chr(idx)
    else :
        answer += i

print(answer)
