try:
    lucros = float(input("Digite o valor dos lucros: "))
    acionistas = int(input("Digite a quantidade de acionistas: "))
    valor_por_acionista = lucros / acionistas
except ValueError:
    print("Digite apenas valores numéricos")
except ZeroDivisionError:
    print("A quantidade de acionistas não pode ser zero")
else:
    print("Valor para cada acionista:", valor_por_acionista)
