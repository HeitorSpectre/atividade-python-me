def calcular_gorjeta(conta):
    return conta * 0.10


valor = float(input("Digite o valor da conta: "))
print("Gorjeta do garçom:", calcular_gorjeta(valor))
