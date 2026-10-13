soma = 0
while True:
    v = float(input("Valor (0 encerra): "))
    if v == 0:
        break
    soma += v
print("Soma:", soma)
