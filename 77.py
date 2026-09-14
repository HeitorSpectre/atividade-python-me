class SaldoInsuficienteError(Exception):
    pass


def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("O valor do saque deve ser positivo")

    if valor_saque > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")

    return saldo - valor_saque


try:
    saldo = float(input("Digite o saldo atual: "))
    valor_saque = float(input("Digite o valor do saque: "))
    novo_saldo = realizar_saque(saldo, valor_saque)
except ValueError as erro:
    print("Erro:", erro)
except SaldoInsuficienteError as erro:
    print("Erro:", erro)
else:
    print("Novo saldo:", novo_saldo)
