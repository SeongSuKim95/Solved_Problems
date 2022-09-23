from math import gcd
def solution(w,h):
    total = w * h
    a = gcd(w, h)
    b = h // a
    c = w // a
    left = total - (b+c-1)*a
    return left