def receber():
    return [float(input("Número: ")) for i in range(5)]

def maior(v):
    return max(v)

def menor(v):
    return min(v)

n=receber()
print(maior(n))
print(menor(n))
