try:
    lucro=float(input("Lucro: "))
    n=int(input("Acionistas: "))
    print(lucro/n)
except ZeroDivisionError:
    print("Quantidade de acionistas não pode ser zero.")
except ValueError:
    print("Dados inválidos.")
