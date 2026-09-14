temperaturas = []

for i in range(5):
    temperatura = float(input("Digite a temperatura do dia: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

print("Média das temperaturas:", media)

if media >= 18 and media <= 28:
    print("A média está dentro da faixa ideal")
else:
    print("A média está fora da faixa ideal")

print("Temperaturas cadastradas:", temperaturas)
