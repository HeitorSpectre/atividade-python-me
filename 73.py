precos = ["10.50", "20", "abc", "35.90", "50"]

for preco in precos:
    try:
        valor = float(preco)
    except ValueError:
        print("Valor inválido:", preco)
    else:
        desconto = valor * 0.10
        valor_final = valor - desconto
        print("Preço com desconto:", valor_final)
