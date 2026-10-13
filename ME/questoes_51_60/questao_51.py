t=[]
for i in range(5):
    t.append(float(input("Temperatura: ")))
media=sum(t)/5
print("Média:",media)
print("Faixa ideal" if 18<=media<=28 else "Fora da faixa")
print(t)
