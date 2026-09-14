def parse_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF com formato inválido")

    return cpf


def main():
    cpf = input("Digite o CPF: ")

    try:
        cpf_formatado = parse_cpf(cpf)
        print("CPF válido:", cpf_formatado)
    except ValueError as erro:
        print(erro)


main()
