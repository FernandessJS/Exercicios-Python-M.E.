def conectar():
    raise ConnectionError("Falha")

def conectar_tentando():
    for i in range(3):
        try:
            conectar()
            return
        except ConnectionError:
            print("Tentativa",i+1,"falhou")
    print("Falha após 3 tentativas")

conectar_tentando()
