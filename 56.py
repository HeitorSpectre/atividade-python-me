quadrado = 1
grao = 1
soma = 0

while quadrado <= 64:
    soma = soma + grao
    print("Quadrado:", quadrado, "tem", grao, "grãos")
    grao = grao * 2
    quadrado = quadrado + 1

print("Total de grãos:", soma)
