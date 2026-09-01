alunos = {}

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

media = sum(alunos.values()) / len(alunos)
print("Média da turma: ", media)

for nome, nota in alunos.items():
    if nota > 7:
        print("Aprovado")