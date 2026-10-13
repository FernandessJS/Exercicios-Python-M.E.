import random
n=random.randint(1,10)
while True:
    t=int(input("Tentativa: "))
    if t==n:
        print("Acertou!")
        break
    print("Maior" if t<n else "Menor")
