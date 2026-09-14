while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            raise ValueError

        print("Idade cadastrada:", idade)
        break
    except ValueError:
        print("Digite uma idade válida")
