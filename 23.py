gastos = []

for i in range(5):
    gasto = float(input("Digite o valor do gasto: "))
    gastos.append(gasto)

print("Total de gastos:", sum(gastos))
