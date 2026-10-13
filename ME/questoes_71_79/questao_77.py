def realizar_saque(saldo,valor_saque):
    if valor_saque<=0:
        raise ValueError("Valor inválido")
    if valor_saque>saldo:
        raise ValueError("Saldo insuficiente")
    return saldo-valor_saque

try:
    print(realizar_saque(100,50))
except ValueError as e:
    print(e)
