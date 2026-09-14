def numero_perfeito(numero):
    if numero <= 1:
        return False

    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i

    return soma == numero


numero = int(input("Digite um número: "))

if numero_perfeito(numero):
    print("É um número perfeito")
else:
    print("Não é um número perfeito")
