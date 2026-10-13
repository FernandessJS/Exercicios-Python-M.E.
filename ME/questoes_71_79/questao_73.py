precos=["10","20.5","abc"]
for p in precos:
    try:
        v=float(p)
    except ValueError:
        print("Valor inválido")
    else:
        print(v*0.9)
