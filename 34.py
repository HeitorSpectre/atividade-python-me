notas = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    notas[nome] = nota

consulta = input("Digite o nome do aluno que deseja consultar: ")

if consulta in notas:
    print("Nota:", notas[consulta])
else:
    print("Aluno não encontrado")
