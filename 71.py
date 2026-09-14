class SaldoInsuficienteError(Exception):
    pass


def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")

    return saldo - valor


saldo = float(input("Digite o saldo atual: "))
valor = float(input("Digite o valor do saque: "))

try:
    novo_saldo = sacar(saldo, valor)
    print("Novo saldo:", novo_saldo)
except SaldoInsuficienteError as erro:
    print(erro)
