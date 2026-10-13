disciplinas=("Matemática","Português")
alunos={}
for i in range(5):
    n=input("Nome: ")
    alunos[n]=(float(input("Matemática: ")),float(input("Português: ")))
for n,(a,b) in alunos.items():
    media=(a+b)/2
    print(n,media,"Aprovado" if media>=7 else "Reprovado")
print(disciplinas)
