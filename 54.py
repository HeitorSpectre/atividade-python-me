estacionamento = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

ocupadas = 0
livres = 0

for linha in estacionamento:
    for vaga in linha:
        if vaga == 1:
            ocupadas = ocupadas + 1
        else:
            livres = livres + 1

print("Vagas ocupadas:", ocupadas)
print("Vagas livres:", livres)
