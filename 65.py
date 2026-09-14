def calcularCubo(numero):
    return numero ** 3


def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    else:
        return False


numero = int(input("Digite um número: "))
print(calcularDivisaoCubo(numero))
