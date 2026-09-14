matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0
for i in range(3):
    soma = soma + matriz[i][i]

print("Soma da diagonal principal:", soma)
