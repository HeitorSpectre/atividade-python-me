matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

soma = 0
for linha in matriz:
    soma = soma + sum(linha)

print("Soma da matriz:", soma)
