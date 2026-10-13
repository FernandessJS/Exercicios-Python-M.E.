def animais(cabecas,pernas):
    coelhos=(pernas-2*cabecas)//2
    galinhas=cabecas-coelhos
    return galinhas,coelhos

print(animais(35,94))
