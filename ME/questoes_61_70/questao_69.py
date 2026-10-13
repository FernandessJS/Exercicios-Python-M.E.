try:
    with open("relatorio_vendas.txt","r") as arq:
        print(arq.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Encerramento do recurso.")
