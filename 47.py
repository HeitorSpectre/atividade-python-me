matriz = [
    [5, -2, 8],
    [-1, 4, 0],
    [7, -3, 2]
]

positivos = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            positivos = positivos + 1

print("Quantidade de valores positivos:", positivos)
