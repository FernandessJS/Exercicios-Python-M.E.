def escolher(a,b):
    return min(a,b) if a%2==0 and b%2==0 else max(a,b)

print(escolher(4,7))
