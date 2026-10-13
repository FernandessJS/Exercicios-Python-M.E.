def blackjack(a,b,c):
    s=a+b+c
    if s<=21:
        return s
    if 11 in (a,b,c):
        s-=10
    return s if s<=21 else -1

print(blackjack(5,6,10))
