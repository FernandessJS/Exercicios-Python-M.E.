alunos={}
for i in range(5):
    n=input("Nome: ")
    alunos[n]=float(input("Nota: "))
print("Média:",sum(alunos.values())/len(alunos))
print("Aprovados:",[n for n,v in alunos.items() if v>=7])
