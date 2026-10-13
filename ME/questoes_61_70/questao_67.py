while True:
    try:
        idade=int(input("Idade: "))
        if idade<0:
            raise ValueError
        break
    except ValueError:
        print("Idade inválida.")
print(idade)
