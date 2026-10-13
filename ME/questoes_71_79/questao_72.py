def parse_cpf(cpf):
    if len(cpf)!=11 or not cpf.isdigit():
        raise ValueError("CPF inválido")
    return cpf

def main():
    try:
        print(parse_cpf(input("CPF: ")))
    except ValueError as e:
        print(e)

main()
