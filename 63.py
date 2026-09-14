def receber_numeros():
    numeros = []

    for i in range(5):
        numero = float(input("Digite um número: "))
        numeros.append(numero)

    return numeros


def maior_numero(numeros):
    return max(numeros)


def menor_numero(numeros):
    return min(numeros)


numeros = receber_numeros()
print("Maior número:", maior_numero(numeros))
print("Menor número:", menor_numero(numeros))
