class ProdutoInvalidoError(Exception):
    pass

class ValorInvalidoError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

def registrar_venda(produto, preco, quantidade):
    if not produto.strip():
        raise ProdutoInvalidoError()
    if preco <= 0:
        raise ValorInvalidoError()
    if not isinstance(quantidade,int) or quantidade <= 0:
        raise QuantidadeInvalidaError()
    return {"produto":produto,"preco":preco,"quantidade":quantidade,"total":preco*quantidade}

def gerar_relatorio(vendas):
    total=sum(v["total"] for v in vendas)
    qtd=len(vendas)
    cont={}
    for v in vendas:
        cont[v["produto"]]=cont.get(v["produto"],0)+v["quantidade"]
    mais=max(cont,key=cont.get) if cont else "Nenhum"
    print("Quantidade de vendas:",qtd)
    print("Produto mais vendido:",mais)
    print("Faturamento:",total)
    print("Ticket médio:",total/qtd if qtd else 0)

vendas=[]
while True:
    produto=input("Produto (fim encerra): ")
    if produto.lower()=="fim":
        break
    try:
        preco=float(input("Preço: "))
        quantidade=int(input("Quantidade: "))
        vendas.append(registrar_venda(produto,preco,quantidade))
    except (ProdutoInvalidoError,ValorInvalidoError,QuantidadeInvalidaError,ValueError) as e:
        print("Erro:",e)
    else:
        print("Venda registrada.")
    finally:
        print("Operação encerrada.")
gerar_relatorio(vendas)
