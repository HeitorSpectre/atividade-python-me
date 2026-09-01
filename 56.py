quadrado = 0
grao = 1
soma = 0

while quadrado <= 63:
    quadrado = quadrado + 1
    if quadrado > 1:
        grao = grao * 2
        soma = soma + grao
    print("\n Quadrado: ", quadrado, " tem ", grao, "grao")