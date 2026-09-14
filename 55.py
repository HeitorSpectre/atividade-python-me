disciplinas = ("Matemática", "Português")
alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    matematica = float(input("Digite a nota de Matemática: "))
    portugues = float(input("Digite a nota de Português: "))

    media = (matematica + portugues) / 2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    alunos[nome] = {
        "Matemática": matematica,
        "Português": portugues,
        "Média": media,
        "Situação": situacao
    }

print("Disciplinas:", disciplinas)

for nome, dados in alunos.items():
    print(nome, "- Média:", dados["Média"], "-", dados["Situação"])
