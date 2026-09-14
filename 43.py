matriz = [
    [12, 45, 8],
    [31, 60, 22],
    [14, 9, 50]
]

maior = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print("Maior valor:", maior)
