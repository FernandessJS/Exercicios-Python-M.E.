def calcular_media(n1,n2,n3):
    if any(n<0 or n>10 for n in (n1,n2,n3)):
        raise ValueError("Nota inválida")
    return (n1+n2+n3)/3

try:
    m=calcular_media(float(input("N1: ")),float(input("N2: ")),float(input("N3: ")))
    print(m,"Aprovado" if m>=7 else "Reprovado")
except (ValueError,TypeError):
    print("Entrada inválida")
