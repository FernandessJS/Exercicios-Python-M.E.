def rota(produtos,id):
    try:
        return produtos[id],200
    except KeyError:
        return "Produto não encontrado",404
    except Exception:
        return "Erro interno",500
