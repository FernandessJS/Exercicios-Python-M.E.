class SaldoInsuficienteError(Exception):
    pass

def saque(saldo,valor):
    if valor>saldo:
        raise SaldoInsuficienteError()
    return saldo-valor
