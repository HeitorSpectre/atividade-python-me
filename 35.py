produtos = {}

for i in range(3):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    produtos[nome] = quantidade

print(produtos)
