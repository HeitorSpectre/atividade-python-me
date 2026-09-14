def calcular_soma(numero1, numero2, numero3):
    soma = numero1 + numero2 + numero3

    if soma > 21 and (numero1 == 11 or numero2 == 11 or numero3 == 11):
        soma = soma - 10

    if soma > 21:
        return -1

    return soma


numero1 = int(input("Digite o primeiro número de 1 a 11: "))
numero2 = int(input("Digite o segundo número de 1 a 11: "))
numero3 = int(input("Digite o terceiro número de 1 a 11: "))

print(calcular_soma(numero1, numero2, numero3))
