import random

numero = random.randint(1, 10)

while True:
    tentativa = int(input("Adivinhe o número de 1 a 10: "))

    if tentativa == numero:
        print("Você acertou")
        break
    elif tentativa < numero:
        print("O número procurado é maior")
    else:
        print("O número procurado é menor")
