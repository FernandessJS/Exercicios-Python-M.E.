def perfeito(n):
    return n>0 and sum(i for i in range(1,n) if n%i==0)==n

print(perfeito(int(input("Número: "))))
