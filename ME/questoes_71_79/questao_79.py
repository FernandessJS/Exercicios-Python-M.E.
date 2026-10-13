def cadastrar_produto(nome,preco,quantidade):
    if not nome.strip():
        raise ValueError("Nome vazio")
    if preco<=0:
        raise ValueError("Preço inválido")
    if quantidade<0:
        raise ValueError("Quantidade inválida")
    return "Produto cadastrado com sucesso."

try:
    print(cadastrar_produto("Arroz",10,5))
except ValueError as e:
    print(e)
