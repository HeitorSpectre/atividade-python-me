notas = []

for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

print("A maior nota é:", max(notas))
