def buscar(perfil,indice):
    try:
        return perfil["permissoes"][indice]
    except (KeyError,IndexError):
        return "acesso_restrito"
