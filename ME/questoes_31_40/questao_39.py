import random
n=random.randint(1,10)
t=int(input("Tentativa: "))
print("Acertou!" if t==n else f"Errou! Era {n}.")
