def calcularCubo(n):
    return n**3

def calcularDivisaoCubo(n):
    return calcularCubo(n) if n%3==0 else False

print(calcularDivisaoCubo(6))
